let svg_ids = []

let get_svg_ids = () => {
    let svg = document.querySelector(`div#svg-product-container svg`);
    if(!svg) { return false; }
    svg_ids = Array.from(svg.querySelectorAll(`[id]`)).map(item => item.id);
    let options = svg_ids.map(opt => `<option value="${opt}"></option>`);
    $(document.body).append($(
        `<datalist id="svp_option_id">${options.join("")}</datalist>`));
}

let create_parte_producto = extra => {
    openPanel($(`#parte-form-template`).html(), "Nueva Parte");
    $(`#main-form-parte input[name="action"]`).val('create-parte');
    $(`#main-form-parte input[name="extra"]`).val(extra);
}

let update_parte_producto = extra =>{
    openPanel($(`#parte-form-template`).html(), "Actualizar Parte");
    let data = $(`#parte-${extra}`)[0].dataset;
    $(`#main-form-parte input[name="action"]`).val('update-parte');
    $(`#main-form-parte input[name="extra"]`).val(extra);
    $(`#main-form-parte input[name="nombre"]`).val(data.nombre);
    $(`#main-form-parte input[name="posicion"]`).val(data.posicion);
    $(`#main-form-parte select[name="tipo_de_parte"]`).val(data.tipo);
    for(let pk of data.paletas.split(',')){
        if(pk && parseInt(pk) > 0) {
            $(`#main-form-parte input[name="paletas_de_color"][value="${pk}"]`).attr('checked', true);
        }
    }
};

let delete_parte_producto = extra =>{
    openPanel($(`#deleting-many-confirmation-template`).html(), "Confirmación de Eliminación");
    let btn = $(`#modal-panel-message button[type="submit"]`);
    let lbl = btn.html();
    let cell = btn.parent();
    btn.remove();
    cell.append($(`<button type="button" onclick="delete_parte_producto_execute(${extra})" class="btn btn-outline-secondary" title="Aceptar">${lbl}</button>`));
};

let delete_parte_producto_execute = (extra) =>{
    let token = $(`#frm-csrfmiddlewaretoken input[name="csrfmiddlewaretoken"]`).val();
    let frm = $(`
        <form method="post" enctype="multipart/form-data">
            <input type="hidden" name="csrfmiddlewaretoken" value="${token}">
            <input type="hidden" name="action" value="delete-parte" />
            <input type="hidden" name="extra" id="extra" value="${extra}" />
        </form>`);
    $(document.body).append(frm);
    frm.submit();
};

let create_campo_parte_producto = extra => {
    openPanel($(`#campo-form-template`).html(), "Nuevo Campo");
    $(`#main-form-campo input[name="action"]`).val('create-campo');
    $(`#main-form-campo input[name="extra"]`).val(extra);
}

let update_campo_parte_producto = extra => {
    openPanel($(`#campo-form-template`).html(), "Actualizar Campo");
    let data = $(`#campo-${extra}`)[0].dataset;
    $(`#main-form-campo input[name="action"]`).val('update-campo');
    $(`#main-form-campo input[name="extra"]`).val(extra);
    $(`#main-form-campo input[name="nombre"]`).val(data.nombre);
    $(`#main-form-campo input[name="id_svg"]`).val(data.idsvg);
    $(`#main-form-campo input[name="posicion"]`).val(data.posicion);
    $(`#main-form-campo select[name="tipo_de_campo"]`).val(data.tipocampo);
    $(`#main-form-campo select[name="opciones_material"]`).val(data.opcionesmaterial);
    $(`#main-form-campo select[name="opciones_color"]`).val(data.opcionescolor);
}

let delete_campo_parte_producto = extra =>{
    openPanel($(`#deleting-many-confirmation-template`).html(), "Confirmación de Eliminación");
    let btn = $(`#modal-panel-message button[type="submit"]`);
    let lbl = btn.html();
    let cell = btn.parent();
    btn.remove();
    cell.append($(`<button type="button" onclick="delete_campo_parte_producto_execute(${extra})" class="btn btn-outline-secondary" title="Aceptar">${lbl}</button>`));
};

let delete_campo_parte_producto_execute = (extra) =>{
    let token = $(`#frm-csrfmiddlewaretoken input[name="csrfmiddlewaretoken"]`).val();
    let frm = $(`
        <form method="post" enctype="multipart/form-data">
            <input type="hidden" name="csrfmiddlewaretoken" value="${token}">
            <input type="hidden" name="action" value="delete-campo" />
            <input type="hidden" name="extra" id="extra" value="${extra}" />
        </form>`);
    $(document.body).append(frm);
    frm.submit();
};

let create_grupo_parte_producto = extra => {
    openPanel($(`#grupo-form-template`).html(), "Nuevo Grupo de Campos");
    $(`#main-form-campo input[name="action"]`).val('create-grupo');
    $(`#main-form-campo input[name="extra"]`).val(extra);
}

let update_grupo_parte_producto = extra => {
    openPanel($(`#grupo-form-template`).html(), "Actualizar Grupo de Campos");
    let data = $(`#grupo-${extra}`)[0].dataset;
    $(`#main-form-campo input[name="action"]`).val('update-grupo');
    $(`#main-form-campo input[name="extra"]`).val(extra);
    $(`#main-form-campo input[name="nombre"]`).val(data.nombre);
    $(`#main-form-campo input[name="posicion"]`).val(data.posicion);
}

let delete_grupo_parte_producto = extra =>{
    openPanel($(`#deleting-many-confirmation-template`).html(), "Confirmación de Eliminación");
    let btn = $(`#modal-panel-message button[type="submit"]`);
    let lbl = btn.html();
    let cell = btn.parent();
    btn.remove();
    cell.append($(`<button type="button" onclick="delete_grupo_parte_producto_execute(${extra})" class="btn btn-outline-secondary" title="Aceptar">${lbl}</button>`));
};

let delete_grupo_parte_producto_execute = (extra) =>{
    let token = $(`#frm-csrfmiddlewaretoken input[name="csrfmiddlewaretoken"]`).val();
    let frm = $(`
        <form method="post" enctype="multipart/form-data">
            <input type="hidden" name="csrfmiddlewaretoken" value="${token}">
            <input type="hidden" name="action" value="delete-grupo" />
            <input type="hidden" name="extra" id="extra" value="${extra}" />
        </form>`);
    $(document.body).append(frm);
    frm.submit();
};

let shown_categories = Array()

let check_show_productos = (pk) => {
    if(pk > 0) {
        if (shown_categories.includes(pk)) {
            shown_categories = shown_categories.filter(item => item !== pk);
            $(`#mnu-cat-opc-${pk} input[type="checkbox"]`).attr('checked', false);
        } else {
            shown_categories.push(pk);
            $(`#mnu-cat-opc-${pk} input[type="checkbox"]`).attr('checked', true);
        }
    }
    let cards = $(`#productos-table div.producto`);
    let txt_find = $(`#txt_find`).val().trim().toUpperCase();
    if(shown_categories.length === 0) {
        cards.removeClass('d-none')
        if(txt_find) {
            Array.from(cards).filter(
                card => !($(card).text().trim().toUpperCase().includes(txt_find))
            ).forEach(card => $(card).addClass('d-none'));
        }
    } else {
        cards.addClass('d-none');
        Array.from(cards).filter(card => {
            let categs = card.dataset.categorias.split(", ").map(value => parseInt(value));
            return categs.filter(c => shown_categories.includes(c)).length > 0;
        }).forEach(card => $(card).removeClass('d-none'));
        if(txt_find) {
            Array.from(cards).filter(
                card => $(card).text().trim().toUpperCase().includes(txt_find)
            ).forEach(card => $(card).removeClass('d-none'));
        }
    }
}

let personalizar_producto = (pk, nombre) => {
    openPanel($(`#producto-personalizacion-${pk}-template`).html(), `Personalizar ${nombre}`);
    $(`.modal-dialog.modal-dialog-centered.modal-lg`).addClass('modal-dialog-scrollable')
}

let paletas_user = {'paletas': 'colores'};

let update_paletas_user = (parte, paleta, color, color_pk, obj) => {
    if(obj.checked) {
        if(! paletas_user[parte]){
            paletas_user[parte] = {'parte': parte}
        }
        if(! paletas_user[parte][paleta]){
            paletas_user[parte][paleta] = {'paleta': paleta, 'colores': Array()}
        }
        paletas_user[parte][paleta]['colores'].push(color);
    } else {
        paletas_user[parte][paleta]['colores'] = paletas_user[parte][paleta]['colores'].filter(c => c !== color);
    }
    let paleta_user = $(`#paleta-parte-${ parte }`);
    if(obj.checked) {
        let label_content = `<div class="d-inline-block muestra-color rounded" style="background-color: ${ color };"></div>`;
        let label = `<label class="btn btn-outline-secondary" for="btn-radio-color-${ color_pk }-paleta-usuario">${label_content}</label>`;
        let radio = `<input type="radio" class="btn-check" name="paleta-parte-${ parte }-color-opc" id="btn-radio-color-${ color_pk }-paleta-usuario" value="${ color_pk }}" autocomplete="off" />`;
        paleta_user.append($(radio));
        paleta_user.append($(label));
    }
};

window.addEventListener('DOMContentLoaded', evt => {
    get_svg_ids();
});
