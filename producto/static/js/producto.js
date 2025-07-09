const DB_NAME = 'PersonalizacionesDB';
const STORE_NAME = 'personalizaciones';

let dbPersonalizaciones = null;

// Función para abrir la base de datos
function openPersonalizacionesDB(callback) {
  if (dbPersonalizaciones) {
    callback(null, dbPersonalizaciones);
    return;
  }
  var req = indexedDB.open(DB_NAME, 1);
  req.onupgradeneeded = function(ev) {
    var db = ev.target.result;
    if (!db.objectStoreNames.contains(STORE_NAME)) {
      db.createObjectStore(STORE_NAME, { keyPath: 'producto_id' });
    }
  };
  req.onerror = function() {
    callback(req.error, null);
  };
  req.onsuccess = function() {
    dbPersonalizaciones = req.result;
    callback(null, dbPersonalizaciones);
  };
}

// Función mejorada para guardar personalización
function savePersonalizacion(producto_id) {
  var form = document.querySelector('#producto-personalizacion-form');
  if (!form) return;

  var campos = {};
  var paletasPersonalizadas = {};
  
  // Recopilar campos del formulario
  Array.from(form.elements).forEach(function(el) {
    if (!el.name) return;

    if (el.type === 'radio') {
      if (el.checked) campos[el.name] = el.value;
    } else if (el.type === 'checkbox') {
      campos[el.name] = el.checked;
    } else {
      campos[el.name] = el.value;
    }
  });

  // Buscar elementos dinámicos sin name pero con ID (checkboxes de paletas)
  var paletaCheckboxes = form.querySelectorAll('input[type="checkbox"][onchange*="update_paletas_user"]');
  paletaCheckboxes.forEach(function(el) {
    if (el.id) {
      campos[el.id] = el.checked;
    }
  });

  // Buscar radios de paletas dinámicos
  var paletaRadios = form.querySelectorAll('input[type="radio"][name*="paleta-parte-"][name*="-color-opc"]');
  paletaRadios.forEach(function(el) {
    if (el.checked && el.name) {
      campos[el.name] = el.value;
    }
  });

  // Guardar estado de paletas personalizadas
  if (window.paletas_user && typeof window.paletas_user === 'object') {
    paletasPersonalizadas = JSON.parse(JSON.stringify(window.paletas_user));
  }

  var timestamp = new Date().getTime();

  openPersonalizacionesDB(function(err, db) {
    if (err) {
      console.error('❌ Error abriendo IndexedDB:', err);
      return;
    }
    var tx = db.transaction(STORE_NAME, 'readwrite');
    var store = tx.objectStore(STORE_NAME);
    var req = store.put({ 
      producto_id: parseInt(producto_id), 
      campos: campos,
      paletas_personalizadas: paletasPersonalizadas,
      timestamp: timestamp,
      completado: false
    });
    req.onerror = function () {
      console.error('❌ Error guardando en IndexedDB:', req.error);
    };
    req.onsuccess = function () {
      console.log(`✅ Personalización guardada para producto ${producto_id}`);
    };
  });
}

// Función mejorada para cargar personalización
function loadPersonalizacion(producto_id, callback) {
  openPersonalizacionesDB(function(err, db) {
    if (err) {
      console.error('❌ Error abriendo IndexedDB:', err);
      callback && callback(err);
      return;
    }
    var tx = db.transaction(STORE_NAME, 'readonly');
    var store = tx.objectStore(STORE_NAME);
    var req = store.get(parseInt(producto_id));
    req.onerror = function () {
      console.error('❌ Error obteniendo datos de IndexedDB:', req.error);
      callback && callback(req.error);
    };
    req.onsuccess = function () {
      var record = req.result;
      if (!record || !record.campos) {
        callback && callback(null); 
        return;
      }

      console.log(`🔍 Recuperando personalización para producto ${producto_id}`);
      
      // Marcar que estamos restaurando
      window.__restoring_from_db = true;
      
      // Restaurar paletas_user en memoria
      if (record.paletas_personalizadas && typeof record.paletas_personalizadas === 'object') {
        window.paletas_user = record.paletas_personalizadas;
      }

      var form = document.querySelector('#producto-personalizacion-form');
      if (!form) {
        callback && callback(null);
        return;
      }

      // Restaurar checkboxes de paletas
      Object.entries(record.campos).forEach(function([name, val]) {
        if (name.includes('paletas') || name.startsWith('btn-check-color')) {
          var els = form.querySelectorAll(`[name="${name}"], #${name}`);
          els.forEach(function(el) {
            if (el.type === 'checkbox') {
              el.checked = !!val;
              el.dispatchEvent(new Event('change', { bubbles: true }));
            }
          });
        }
      });

      // Esperar y verificar reconstrucción
      setTimeout(function() {
        var paletaContainer = document.querySelector('#paleta-parte-24');
        var paletaContainer88 = document.querySelector('#paleta-parte-88');
        
        function reconstructPaletasUIParte(parte) {
          if (!window.paletas_user || typeof window.paletas_user !== 'object') return;

          var paletasParte = window.paletas_user[parte];
          var paleta_container = document.querySelector(`#paleta-parte-${parte}`);
          if (!paletasParte || !paleta_container) return;

          paleta_container.innerHTML = '';

          Object.keys(paletasParte).forEach(function(key) {
            if (key === 'parte') return;

            var paleta = paletasParte[key];
            if (paleta && Array.isArray(paleta.colores)) {
              paleta.colores.forEach(function(color, index) {
                var color_pk = `${parte}_${key}_${index}`;
                var radio_value = `${color}||Color ${color}||${color}`;
                var label_content = `<div class="d-inline-block muestra-color rounded" style="background-color: ${color}; width: 20px; height: 20px; border: 1px solid #ccc;"></div>`;
                var label = `<label class="border-0 btn btn-outline-secondary me-1" for="btn-radio-color-${color_pk}-paleta-usuario" title="Color ${color}">${label_content}</label>`;
                var radio = `<input type="radio" class="btn-check" name="paleta-parte-${parte}-color-opc" id="btn-radio-color-${color_pk}-paleta-usuario" value="${radio_value}" autocomplete="off" />`;

                paleta_container.innerHTML += radio + label;
              });
            }
          });
        }
        
        if (paletaContainer88 && paletaContainer88.children.length === 0) {
          reconstructPaletasUIParte('88');
        }
        if (paletaContainer && paletaContainer.children.length === 0) {
          reconstructPaletasUI();
        }
        
        // Forzar reconstrucción usando método que funcionaba
        setTimeout(function() {
          var paleta_container = document.querySelector('#paleta-parte-24');
          if (paleta_container) {
            paleta_container.innerHTML = '';
            
            if (window.paletas_user && window.paletas_user['24']) {
              var paletas_24 = window.paletas_user['24'];
              
              Object.keys(paletas_24).forEach(function(key) {
                if (key === 'parte') return;
                
                var paleta = paletas_24[key];
                
                if (paleta && paleta.colores && Array.isArray(paleta.colores)) {
                  paleta.colores.forEach(function(color, index) {
                    var color_pk = `24_${key}_${index}`;
                    var radio_value = `${color}||Color ${color}||${color}`;
                    var label_content = `<div class="d-inline-block muestra-color rounded" style="background-color: ${color}; width: 20px; height: 20px; border: 1px solid #ccc;"></div>`;
                    var label = `<label class="border-0 btn btn-outline-secondary me-1" for="btn-radio-color-${color_pk}-paleta-usuario" title="Color ${color}">${label_content}</label>`;
                    var radio = `<input type="radio" class="btn-check" name="paleta-parte-24-color-opc" id="btn-radio-color-${color_pk}-paleta-usuario" value="${radio_value}" autocomplete="off" />`;
                    
                    paleta_container.innerHTML += radio + label;
                  });
                }
              });
            }
          }
          
          //Restaurar otros campos
          setTimeout(function() {
            Object.entries(record.campos).forEach(function([name, val]) {
              if (!name.includes('paletas') && !name.startsWith('btn-check-color')) {
                var els = form.querySelectorAll(`[name="${name}"]`);
                
                if (els.length > 0) {
                  els.forEach(function(el) {
                    if (el.type === 'checkbox') {
                      el.checked = !!val;
                      el.dispatchEvent(new Event('change', { bubbles: true }));
                    } else if (el.type === 'radio') {
                      el.checked = (el.value === val);
                      if (el.checked) {
                        el.dispatchEvent(new Event('change', { bubbles: true }));
                        
                        // Aplicar a SVG si es campo de color
                        try {
                          if (typeof update_picture_color === 'function') {
                            let id_svg = el.dataset.idSvg || null;
                            let pkparte = el.dataset.pkParte || null;
                            if (id_svg && pkparte) {
                              update_picture_color(el, pkparte, id_svg);
                            }
                          }
                        } catch(e) {
                          console.warn('⚠️ Error actualizando SVG:', e);
                        }
                      }
                    } else {
                      el.value = val;
                      el.dispatchEvent(new Event('input', { bubbles: true }));
                    }
                  });
                } else {
                  console.warn(`❌ No se encontraron elementos para ${name}`);
                }
              }
            });
            // Restaurar selección de paleta
            var paletaField = 'paleta-parte-24-color-opc';
            var savedPaletaValue = record.campos[paletaField];
            if (savedPaletaValue) {
              console.log(`🎨 Restaurando selección de paleta: ${savedPaletaValue}`);
              
              var colorMatch = savedPaletaValue.split('||')[0];
              var paletaContainer = document.querySelector('#paleta-parte-24');
              
              if (paletaContainer) {
                var radios = paletaContainer.querySelectorAll('input[type="radio"]');
                var foundRadio = Array.from(radios).find(function(radio) {
                  return radio.value.startsWith(colorMatch);
                });
                
                if (foundRadio) {
                  console.log(`🎯 Aplicando selección a: ${foundRadio.id}`);
                  
                  foundRadio.checked = true;
                  foundRadio.setAttribute('checked', 'checked');
                  foundRadio.dispatchEvent(new Event('change', { bubbles: true }));
                  foundRadio.dispatchEvent(new Event('click', { bubbles: true }));
                  
                  var associatedLabel = document.querySelector(`label[for="${foundRadio.id}"]`);
                  if (associatedLabel) {
                    var allLabels = document.querySelectorAll('#paleta-parte-24 label');
                    allLabels.forEach(label => label.classList.remove('active', 'btn-check-active'));
                    
                    associatedLabel.classList.add('active', 'btn-check-active');
                    associatedLabel.click();
                  }
                  var paletaField88 = 'paleta-parte-88-color-opc';
                  var savedPaletaValue88 = record.campos[paletaField88];
                  if (savedPaletaValue88) {
                    var colorMatch88 = savedPaletaValue88.split('||')[0];
                    var paletaContainer88 = document.querySelector('#paleta-parte-88');
                    
                    if (paletaContainer88) {
                      var radios88 = paletaContainer88.querySelectorAll('input[type="radio"]');
                      var foundRadio88 = Array.from(radios88).find(radio => radio.value.startsWith(colorMatch88));

                      if (foundRadio88) {
                        foundRadio88.checked = true;
                        foundRadio88.setAttribute('checked', 'checked');
                        foundRadio88.dispatchEvent(new Event('change', { bubbles: true }));
                        foundRadio88.dispatchEvent(new Event('click', { bubbles: true }));

                        var associatedLabel88 = document.querySelector(`label[for="${foundRadio88.id}"]`);
                        if (associatedLabel88) {
                          var allLabels88 = document.querySelectorAll('#paleta-parte-88 label');
                          allLabels88.forEach(label => label.classList.remove('active', 'btn-check-active'));

                          associatedLabel88.classList.add('active', 'btn-check-active');
                          associatedLabel88.click();
                        }

                        // Aplicar color a campos SVG 
                        setTimeout(function() {
                          var colorFields88 = document.querySelectorAll('input[onchange*="update_picture_color"]');
                          colorFields88.forEach(function(field) {
                            try {
                              var onchangeAttr = field.getAttribute('onchange');
                              if (onchangeAttr && onchangeAttr.includes(', 88,')) {
                                field.value = foundRadio88.value;
                                field.checked = true;
                                field.dispatchEvent(new Event('change', { bubbles: true }));
                                console.log(`✅ Color aplicado a ${field.id}`);
                              }
                            } catch(e) {
                              console.warn(`⚠️ Error aplicando color a campo ${field.id}:`, e);
                            }
                          });
                        }, 100);
                      } else {
                        console.warn(`❌ No se encontró radio para color (88): ${colorMatch88}`);
                      }
                    }
                  }
                  
                  setTimeout(function() {
                    var colorFields = document.querySelectorAll('input[onchange*="update_picture_color"]');
                    
                    colorFields.forEach(function(field) {
                      try {
                        var onchangeAttr = field.getAttribute('onchange');
                        if (onchangeAttr && onchangeAttr.includes(', 24,')) {
                          console.log(`🎯 Aplicando color a campo: ${field.id}`);
                          
                          field.value = foundRadio.value;
                          field.checked = true;
                          field.dispatchEvent(new Event('change', { bubbles: true }));
                          
                          console.log(`✅ Color aplicado a ${field.id}`);
                        }
                      } catch(e) {
                        console.warn(`⚠️ Error aplicando color a campo ${field.id}:`, e);
                      }
                    });
                  }, 100);
                  
                } else {
                  console.warn(`❌ No se encontró radio para color: ${colorMatch}`);
                }
              }
            }
            
            window.__restoring_from_db = false;
            console.log('✅ Carga de personalización completada');
            
            callback && callback(null);
            showRecoveryNotification(record.timestamp);
            
          }, 300);
        }, 200);
      }, 400);
    };
  });
}

// Función para reconstruir la UI de paletas
function reconstructPaletasUI() {
  if (!window.paletas_user || typeof window.paletas_user !== 'object') return;
  
  Object.keys(window.paletas_user).forEach(function(parte) {
    if (parte === 'paletas') return;
    
    var paletaData = window.paletas_user[parte];
    if (!paletaData || !paletaData.colores) return;
    
    var paleta_container = document.querySelector(`#paleta-parte-${parte}`);
    if (!paleta_container) return;
    
    paleta_container.innerHTML = '';
    
    paletaData.colores.forEach(function(color) {
      var originalCheckbox = document.querySelector(`input[type="checkbox"][name^="paletas"][value="${color}"]`);
      if (originalCheckbox && originalCheckbox.checked) {
        var color_pk = originalCheckbox.dataset.colorPk || '';
        var paleta_name = originalCheckbox.dataset.paletaName || '';
        var color_name = originalCheckbox.dataset.colorName || '';
        var color_code = originalCheckbox.dataset.colorCode || color;
        
        var radio_value = `${color}||${color_name}||${color_code}`;
        var label_content = `<div class="d-inline-block muestra-color rounded" style="background-color: ${color};"></div>`;
        var label = `<label class="border-0 btn btn-outline-secondary" for="btn-radio-color-${color_pk}-paleta-usuario" title="${paleta_name} - ${color_name}">${label_content}</label>`;
        var radio = `<input type="radio" class="btn-check" name="paleta-parte-${parte}-color-opc" id="btn-radio-color-${color_pk}-paleta-usuario" value="${radio_value}" autocomplete="off" />`;
        
        paleta_container.innerHTML += radio + label;
      }
    });
  });
}

// Funciones auxiliares
function showRecoveryNotification(timestamp) {
  var fecha = new Date(timestamp);
  var fechaFormateada = fecha.toLocaleDateString() + ' ' + fecha.toLocaleTimeString();
  
  var notification = document.createElement('div');
  notification.className = 'alert alert-info alert-dismissible fade show position-fixed';
  notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; max-width: 400px;';
  notification.innerHTML = `
    <i class="fas fa-info-circle"></i>
    <strong>Personalización recuperada</strong><br>
    Se ha restaurado tu personalización anterior del ${fechaFormateada}
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
  `;
  
  document.body.appendChild(notification);
  
  setTimeout(function() {
    if (notification.parentNode) {
      notification.remove();
    }
  }, 5000);
}

function checkPersonalizacionesIncompletas() {
  openPersonalizacionesDB(function(err, db) {
    if (err) return;
    
    var tx = db.transaction(STORE_NAME, 'readonly');
    var store = tx.objectStore(STORE_NAME);
    var req = store.getAll();
    
    req.onsuccess = function() {
      var records = req.result;
      var incompletas = records.filter(r => !r.completado);
      
      if (incompletas.length > 0) {
        addPersonalizacionesIndicator(incompletas);
      }
    };
  });
}

function addPersonalizacionesIndicator(personalizaciones) {
  personalizaciones.forEach(function(p) {
    var productoElement = document.querySelector(`[data-producto-id="${p.producto_id}"]`);
    if (productoElement) {
      var indicator = document.createElement('div');
      indicator.className = 'badge bg-warning position-absolute';
      indicator.style.cssText = 'top: 5px; right: 5px; font-size: 0.7em;';
      indicator.innerHTML = '<i class="fas fa-clock"></i> Incompleta';
      indicator.title = 'Tienes una personalización incompleta';
      
      productoElement.style.position = 'relative';
      productoElement.appendChild(indicator);
    }
  });
}

function markPersonalizacionCompleted(producto_id) {
  openPersonalizacionesDB(function(err, db) {
    if (err) return;
    
    var tx = db.transaction(STORE_NAME, 'readwrite');
    var store = tx.objectStore(STORE_NAME);
    var req = store.delete(parseInt(producto_id));
    
    req.onsuccess = function() {
      console.log(`✅ Personalización completada para producto ${producto_id}`);
    };
  });
}

// INTEGRACIÓN CON LA FUNCIÓN personalizar_producto MODERNA CON AUTO-GUARDADO
document.addEventListener('DOMContentLoaded', function() {
  var original_personalizar = window.personalizar_producto;
  
  personalizar_producto = function(pk, nombre) {
    paletas_user = {'paletas': 'colores'};
    
    if (original_personalizar && typeof original_personalizar === 'function') {
      original_personalizar(pk, nombre);
    } else {
      var template = document.querySelector(`#producto-personalizacion-${pk}-template`);
      if (template) {
        openPanel(template.innerHTML, `Personalizar ${nombre}`);
      } else {
        console.warn('No se encontró template ni función original para personalizar producto');
        return;
      }
    }

    function waitForForm() {
      var form = document.querySelector('#producto-personalizacion-form');
      if (!form) {
        return setTimeout(waitForForm, 100);
      }

      // Agregar clase para scroll en modal
      setTimeout(function() {
        var modalDialog = document.querySelector('.modal-dialog.modal-dialog-centered.modal-lg');
        if (modalDialog) {
          modalDialog.classList.add('modal-dialog-scrollable');
        }
      }, 50);

      if (!form._listenersAdded) {
        form._listenersAdded = true;
        
        // Función para agregar listeners con throttling
        function addSaveListener(element, eventType) {
          var saveTimeout;
          element.addEventListener(eventType, function(e) {
            if (!window.__restoring_from_db) {
              clearTimeout(saveTimeout);
              saveTimeout = setTimeout(() => {
                savePersonalizacion(pk);
              }, 300);
            }
          });
        }
        
        // Agregar listeners a elementos existentes
        var formElements = form.querySelectorAll('input, select, textarea');
        
        formElements.forEach(function(el) {
          if (el.name || el.id) {
            addSaveListener(el, 'change');
            if (['text', 'number', 'email', 'tel'].includes(el.type) || el.tagName === 'TEXTAREA') {
              addSaveListener(el, 'input');
            }
          }
        });

        // Agregar listeners específicos para checkboxes de paletas SIN name
        var paletaCheckboxes = form.querySelectorAll('input[type="checkbox"][onchange*="update_paletas_user"]');
        
        paletaCheckboxes.forEach(function(el) {
          if (!el._listenerAdded) {
            el._listenerAdded = true;
            addSaveListener(el, 'change');
          }
        });

        // Observer para elementos agregados dinámicamente
        var observer = new MutationObserver(function(mutations) {
          mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
              if (node.nodeType === 1) {
                var newInputs = [];
                if (node.matches && node.matches('input, select, textarea')) {
                  newInputs = [node];
                } else if (node.querySelectorAll) {
                  newInputs = Array.from(node.querySelectorAll('input, select, textarea'));
                }
                
                newInputs.forEach(function(el) {
                  if ((el.name || el.id) && !el._listenerAdded) {
                    el._listenerAdded = true;
                    addSaveListener(el, 'change');
                    if (['text', 'number', 'email', 'tel'].includes(el.type) || el.tagName === 'TEXTAREA') {
                      addSaveListener(el, 'input');
                    }
                  }
                });
              }
            });
          });
        });

        observer.observe(form, {
          childList: true,
          subtree: true
        });

        // Llamar a conectarPaletas
        setTimeout(conectarPaletas, 100);

        // Listener para submit
        form.addEventListener('submit', function() {
          markPersonalizacionCompleted(pk);
        });
      }

      // Cargar datos guardados
      setTimeout(() => {
        window.__restoring_from_db = true;
        loadPersonalizacion(pk, function(err) {
          window.__restoring_from_db = false;
          if (err) {
            console.error('❌ Error cargando personalización:', err);
          }
        });
      }, 300);
    }
    waitForForm();
  };
  
  // Verificar personalizaciones incompletas al cargar la página
  setTimeout(checkPersonalizacionesIncompletas, 1000);
});

// Función conectarPaletas mejorada
function conectarPaletas() {
  var checkboxesPaletas = document.querySelectorAll('input[type=checkbox][onchange*="update_paletas_user"]');
  
  checkboxesPaletas.forEach(function(chk, index) {
    if (!chk._paletaListenerAdded) {
      chk._paletaListenerAdded = true;
      
      chk.addEventListener('change', function(e) {
        if (!window.__restoring_from_db) {
          // Extraer parámetros del atributo onchange
          try {
            var onchangeAttr = this.getAttribute('onchange');
            
            var match = onchangeAttr.match(/update_paletas_user\(([^)]+)\)/);
            if (match) {
              var params = match[1].split(',').map(p => p.trim().replace(/['"]/g, ''));
              var parte = params[0] || 'default_parte';
              var paleta = params[1] || 'default_paleta';
              var color = params[2] || '';
              var color_pk = params[3] || '';
              var paleta_name = params[5] || '';
              var color_name = params[6] || '';
              var color_code = params[7] || '';

              // Manejar habilitación/deshabilitación de colores por COLOR HEX
              if (this.checked) {
                // Deshabilitar otros checkboxes que tengan el mismo color HEX
                document.querySelectorAll(`input[type=checkbox][onchange*="update_paletas_user"]`).forEach(otherChk => {
                  if (otherChk !== this) {
                    try {
                      var otherOnchange = otherChk.getAttribute('onchange');
                      var otherMatch = otherOnchange.match(/update_paletas_user\(([^)]+)\)/);
                      if (otherMatch) {
                        var otherParams = otherMatch[1].split(',').map(p => p.trim().replace(/['"]/g, ''));
                        var otherColor = otherParams[2];
                        
                        if (otherColor === color) {
                          otherChk.disabled = true;
                          otherChk.parentElement.style.opacity = '0.5';
                          otherChk.parentElement.style.pointerEvents = 'none';
                        }
                      }
                    } catch(e) {
                      console.warn('⚠️ Error comparando colores:', e);
                    }
                  }
                });
              } else {
                // Habilitar otros checkboxes que tengan el mismo color HEX
                document.querySelectorAll(`input[type=checkbox][onchange*="update_paletas_user"]`).forEach(otherChk => {
                  if (otherChk !== this) {
                    try {
                      var otherOnchange = otherChk.getAttribute('onchange');
                      var otherMatch = otherOnchange.match(/update_paletas_user\(([^)]+)\)/);
                      if (otherMatch) {
                        var otherParams = otherMatch[1].split(',').map(p => p.trim().replace(/['"]/g, ''));
                        var otherColor = otherParams[2];
                        
                        if (otherColor === color) {
                          otherChk.disabled = false;
                          otherChk.parentElement.style.opacity = '';
                          otherChk.parentElement.style.pointerEvents = '';
                        }
                      }
                    } catch(e) {
                      console.warn('⚠️ Error habilitando colores:', e);
                    }
                  }
                });
              }

              // Llamar a la función update_paletas_user original
              if (typeof update_paletas_user === 'function') {
                update_paletas_user(parte, paleta, color, color_pk, this, paleta_name, color_name, color_code);
              }
            }
          } catch(e) {
            console.warn('⚠️ Error procesando cambio de paleta:', e);
          }
        }
      });
    }
  });
}

if (typeof window.paletas_user === 'undefined') {
  window.paletas_user = {'paletas': 'colores'};
}

// Función update_paletas_user con prevención de duplicados
let update_paletas_user = (parte, paleta, color, color_pk, obj, paleta_name, color_name, color_code) => {
  if(obj.checked) {
    if(! paletas_user[parte]){
      paletas_user[parte] = {'parte': parte}
    }
    if(! paletas_user[parte][paleta]){
      paletas_user[parte][paleta] = {'paleta': paleta, 'colores': Array()}
    }
    // Evitar duplicados - solo agregar si no existe
    if (!paletas_user[parte][paleta]['colores'].includes(color)) {
      paletas_user[parte][paleta]['colores'].push(color);
    }
  } else {
    if (paletas_user[parte] && paletas_user[parte][paleta] && paletas_user[parte][paleta]['colores']) {
      paletas_user[parte][paleta]['colores'] = paletas_user[parte][paleta]['colores'].filter(c => c !== color);
    }
  }
  
  let paleta_user = $(`#paleta-parte-${ parte }`);
  if (!paleta_user.length) return;
  
  if(obj.checked) {
    // Verificar si el radio ya existe para evitar duplicados
    let existingRadio = paleta_user.find(`#btn-radio-color-${ color_pk }-paleta-usuario`);
    if (existingRadio.length === 0) {
      let radio_value = `${color}||${color_name}||${color_code}`;
      let label_content = `<div class="d-inline-block muestra-color rounded" style="background-color: ${ color }; width: 20px; height: 20px; border: 1px solid #ccc;"></div>`;
      let label = `<label class="border-0 btn btn-outline-secondary me-1" for="btn-radio-color-${ color_pk }-paleta-usuario" title="${paleta_name} - ${color_name}">${label_content}</label>`;
      let radio = `<input type="radio" class="btn-check" name="paleta-parte-${ parte }-color-opc" id="btn-radio-color-${ color_pk }-paleta-usuario" value="${ radio_value }" autocomplete="off" />`;
      paleta_user.append($(radio));
      paleta_user.append($(label));
    }
  } else {
    $(`#paleta-parte-${ parte } label[for="btn-radio-color-${ color_pk }-paleta-usuario"]`).remove();
    $(`#paleta-parte-${ parte } input#btn-radio-color-${ color_pk }-paleta-usuario`).remove();
  }
};

// Función update_picture_color mejorada
let update_picture_color = (check, pkparte, id_svg) => {
  var color_checked = Array.from($(`input[name="paleta-parte-${pkparte}-color-opc"]`)).filter(radio => radio.checked);
  check.checked = false;
  if(color_checked.length == 0) {
    alert("Debe seleccionar al menos un color de la paleta de colores para personalizar el producto.");
    return false;
  }
  var div_color = $(`label[for="${color_checked[0].id}"] div.muestra-color`)[0];
  if (!div_color) {
    console.warn('❌ No se encontró div.muestra-color para:', color_checked[0].id);
    return false;
  }
  
  var color_text = div_color.style.backgroundColor;
  check.value = color_checked[0].value;
  check.checked = true; 
  
  var div_color_campo = $(`label[for="${check.id}"] div.muestra-color`)[0];
  if (div_color_campo) {
    div_color_campo.style.backgroundColor = color_text;
  }
  var svg_item = $(`#producto-svg svg #${id_svg}`)[0];
  if (svg_item) {
    svg_item.style.fill = color_text;
  }
  
  check.dispatchEvent(new Event('change', { bubbles: true }));
  
  return true;
};

// Funciones auxiliares originales
window.update_selectable_values_label = function() {
  var form = document.querySelector('form#producto-personalizacion-form');
  if (!form) return;
  
  var selectableValues = Array.from(form.querySelectorAll('input.selectable-value')).filter(
    input => input.checked).map(input => input.value).join(",");
  
  var label = document.querySelector('#label-producto-personalizado');
  if (label) {
    label.innerHTML = selectableValues;
  }
};

window.update_color_fields = function() {
  var form = document.querySelector('form#producto-personalizacion-form');
  if (!form) return false;
  
  var campos_color = {};
  Array.from(form.querySelectorAll('input[type="checkbox"][name^="campo-"]')).forEach(
    input => campos_color[input.name] = input.value);
  
  var camposColorInput = form.querySelector('input#campos_color');
  if (camposColorInput) {
    camposColorInput.value = JSON.stringify(campos_color);
  }
  
  setTimeout(() => {
    closePanel();
    setTimeout(() => {
      openPanel(
        'En un momento comenzará la descarga del formato para el producto personalizado',
        'Descargando...');
    }, 1000);
  }, 1000);
  return true;
};

window.update_picture_color_2 = function(input, id_svg) {
  if(id_svg) {
    var svg_item = document.querySelector(`#producto-svg svg #${id_svg}`);
    if (svg_item) {
      svg_item.style.fill = input.value;
    }
  }
};

// Función para aplicar color seleccionado a campos correspondientes
window.applySelectedColorToFields = function(parte) {
  var paletaContainer = document.querySelector(`#paleta-parte-${parte}`);
  if (!paletaContainer) {
    console.warn(`No se encontró contenedor de paleta para parte ${parte}`);
    return false;
  }
  
  var selectedRadio = paletaContainer.querySelector('input[type="radio"]:checked');
  if (!selectedRadio) {
    console.warn(`No hay color seleccionado en paleta de parte ${parte}`);
    return false;
  }
  
  var colorFields = document.querySelectorAll(`input[onchange*="update_picture_color"][onchange*=", ${parte},"]`);
  
  var appliedCount = 0;
  colorFields.forEach(function(field) {
    try {
      field.value = selectedRadio.value;
      field.checked = true;
      field.dispatchEvent(new Event('change', { bubbles: true }));
      
      appliedCount++;
    } catch(e) {
      console.error(`Error aplicando color a ${field.id}:`, e);
    }
  });
  
  return appliedCount > 0;
};

// Función testReconstruccion para debug
window.testReconstruccion = function() {
  var container = document.querySelector('#paleta-parte-24');
  
  if (container) {
    container.innerHTML = '';
    
    var paletas_24 = window.paletas_user['24'];
    
    if (paletas_24) {
      Object.keys(paletas_24).forEach(function(key) {
        if (key === 'parte') return;
        
        var paleta = paletas_24[key];
        
        if (paleta && paleta.colores && Array.isArray(paleta.colores)) {
          paleta.colores.forEach(function(color, index) {
            var color_pk = `24_${key}_${index}`;
            var radio_value = `${color}||Color ${color}||${color}`;
            var label_content = `<div class="d-inline-block muestra-color rounded" style="background-color: ${color}; width: 20px; height: 20px; border: 1px solid #ccc;"></div>`;
            var label = `<label class="border-0 btn btn-outline-secondary me-1" for="btn-radio-color-${color_pk}-paleta-usuario" title="Color ${color}">${label_content}</label>`;
            var radio = `<input type="radio" class="btn-check" name="paleta-parte-24-color-opc" id="btn-radio-color-${color_pk}-paleta-usuario" value="${radio_value}" autocomplete="off" />`;
            
            container.innerHTML += radio + label;
          });
        }
      });
    }
  }
};

// Verificar que openPanel existe
if (typeof window.openPanel !== 'function') {
  console.warn('⚠️ openPanel no definida, creando función básica');
  
  window.openPanel = function(content, title) {
    var existingModal = document.getElementById('modal-panel-message');
    if (existingModal) existingModal.remove();
    
    var modal = document.createElement('div');
    modal.id = 'modal-panel-message';
    modal.className = 'modal fade show';
    modal.style.display = 'block';
    modal.setAttribute('aria-hidden', 'false');
    modal.innerHTML = `
      <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">${title}</h5>
            <button type="button" class="btn-close" onclick="closePanel()" aria-label="Cerrar"></button>
          </div>
          <div class="modal-body">${content}</div>
        </div>
      </div>
      <div class="modal-backdrop fade show"></div>
    `;
    document.body.appendChild(modal);
  };
  
  window.closePanel = function() {
    var modal = document.getElementById('modal-panel-message');
    if (modal) modal.remove();
  };
}

console.log('🎯 Sistema de personalización cargado');