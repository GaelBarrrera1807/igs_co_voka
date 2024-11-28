let create_tipo_opcion = () => {
    openPanel($(`#opction-form-template`).html(), "Nueva Opción");
    $(`#main-form-option input[name="action"]`).val('create')
}

let delete_tipo_opcion = () => {
    cbk = Array.from($(`#main-data-table input[type="checkbox"]`)).filter(item => item.checked);
    if(cbk.length > 0) {
        delete_many_records();
        let btn = $(`#modal-panel-message button[type="submit"]`);
        let lbl = btn.html();
        let cell = btn.parent();
        btn.remove();
        cell.append($(`<button type="button" onclick="delete_tipo_opcion_execute()" class="btn btn-outline-secondary" title="Aceptar">${lbl}</button>`));
    }
}

let delete_tipo_opcion_execute = () => {
    cbk = Array.from($(`#main-data-table input[type="checkbox"]`)).filter(item => item.checked).map(item => item.value);
    let token = $(`#frm-csrfmiddlewaretoken input[name="csrfmiddlewaretoken"]`).val();
    let frm = $(`
        <form method="post" enctype="multipart/form-data">
            <input type="hidden" name="csrfmiddlewaretoken" value="${token}">
            <input type="hidden" name="action" value="delete" />
            <input type="hidden" name="extra" id="extra" value="${cbk.join(',')}" />
        </form>`);
    $(document.body).append(frm);
    frm.submit();
}

let update_tipocolor_opcion = () => {
    cbk = Array.from($(`#main-data-table input[type="checkbox"]`)).filter(item => item.checked);
    if(cbk.length > 0) {
        let id = cbk[0].value;
        let color = $(cbk[0]).parent().parent().find("td:nth-child(2)").text();
        openPanel($(`#opction-form-template`).html(), "Actualizar Opción");
        $(`#main-form-option input[name="action"]`).val('update')
        $(`#main-form-option input[name="color"]`).val(color)
        $(`#main-form-option #extra`).val(id);
    }
}

let update_tipomaterial_opcion = () => {
    cbk = Array.from($(`#main-data-table input[type="checkbox"]`)).filter(item => item.checked);
    if(cbk.length > 0) {
        let id = cbk[0].value;
        let material = $(cbk[0]).parent().parent().find("td:nth-child(2)").text();
        openPanel($(`#opction-form-template`).html(), "Actualizar Opción");
        $(`#main-form-option input[name="action"]`).val('update')
        $(`#main-form-option input[name="material"]`).val(material)
        $(`#main-form-option #extra`).val(id);
    }
}
