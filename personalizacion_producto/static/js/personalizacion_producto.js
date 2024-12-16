let show_form_set_value_campo_personalizacion = pkcampo => {
    let control = $(`#form-control-${pkcampo}-template`).html();
    let template = Handlebars.compile($("#form-control-update-template").html());
    let body = template({control, pkcampo});
    openPanel(body, "Actualización de Valor de Campo de Personalización");
}
