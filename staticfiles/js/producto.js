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

let check_show_productos = () => {
    let ckb = Array.from(document.querySelectorAll(`input.category-type[type="checkbox"]`)).filter(item => item.checked);
    let cards = $(`#productos-table div.producto`);
    if(ckb.length === 0) {
        cards.removeClass('d-none')
    } else {
        cards.addClass('d-none');
        let ids = ckb.map(item => item.dataset.categoryId);
        Array.from(cards).filter(card => {
            let categs = card.dataset.categorias.split(", ");
            return categs.filter(c => ids.includes(c)).length > 0;
        }).forEach(card => $(card).removeClass('d-none'));
    }
}

window.addEventListener('DOMContentLoaded', evt => {
    get_svg_ids();
});
