const regex_spaces = /\s{2}/g;
const regex_nl = /\n/g

let delete_fav = () => {
    let url = location.href;
    let csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
    $.post(
        usr_delete_fav_url, {csrfmiddlewaretoken, url},
        response => $(`#menu-favs-items`).html(
            `<div class="app-heading">Mis Favoritos</div>${response}`
        )).fail(ajax_failure).always(check_is_fav);
};

let add_2_fav = () => {
    let etiqueta = $(`#page-title`).text().trim().replaceAll(
        regex_nl, " ").replaceAll(regex_spaces, " ");
    while(etiqueta.search(regex_spaces) > -1) {
        etiqueta = etiqueta.replaceAll(regex_spaces, " ");
    }
    let url = location.href;
    let csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
    $.post(
        usr_add_fav_url, {csrfmiddlewaretoken, url, etiqueta},
        response => $(`#menu-favs-items`).html(
            `<div class="app-heading">Mis Favoritos</div>${response}`
        )).fail(ajax_failure).always(check_is_fav);
};

let check_is_fav = () => {
    $("button.fav-out").removeClass('d-none');
    $("button.fav-in").addClass('d-none');
    for(let lnk of $(`.sb-sidenav-menu-favs a.fav-lnk`)) {
        if(lnk.href === location.href) {
            $("button.fav-in").removeClass('d-none');
            $("button.fav-out").addClass('d-none');
            break;
        }
    }
}

window.addEventListener('DOMContentLoaded', check_is_fav);
