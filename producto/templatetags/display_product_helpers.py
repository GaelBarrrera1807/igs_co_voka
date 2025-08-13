from typing import Iterable

from django import template

from catalogo.models import CategoriaProducto
from producto.models import CampoParteProducto
from producto.models import ParteProducto
from producto.models import Producto

register = template.Library()

@register.inclusion_tag("producto/display/table.html", takes_context=True)
def display_product_table(context) -> dict:
    return {"products":
                list(Producto.objects.filter(mostrar_en_galeria=True)),
            "MEDIA_URL": context.get('MEDIA_URL'),
            "context": context,
            "categories":
                list([
                    categoria
                    for categoria in CategoriaProducto.objects.all()
                    if len(categoria.productos.all()) > 0]),
            }


@register.inclusion_tag("producto/display/categories.html")
def display_product_categories_tree() -> dict:
    return {"categories":
                list(CategoriaProducto.objects.filter(categoria_padre=None))}


@register.inclusion_tag("campo/control/input.html")
def field_control_input(
        id: str, value: str, title: str = "", type: str = "text") -> dict:
    return {"id": id, "value": value, "title": title, "type": type, }


@register.inclusion_tag("campo/control/select.html")
def field_control_select(
        id: str, value: str, opciones: Iterable, title: str = "") -> dict:
    opcs = [str(opc) for opc in opciones]
    return {"id": id, "value": value, "title": title, "opcs": opcs, }


@register.inclusion_tag("campo/control/select_color.html")
def field_control_select_color(
        id: str, value: str, opciones: Iterable, ) -> dict:
    vname, vcolor = value.split("|") if "|" in value else ("", "")
    return {"id": id, "value": value, "opcs": opciones, "vcolor": vcolor, "vname": vname}


@register.inclusion_tag("campo/control/form_control.html")
def form_field_control(campo: CampoParteProducto, value: str = "") -> dict:
    return {
        'campo': campo, 'value': value,
        'id': f'campo-html-object-{campo.pk}', }

@register.inclusion_tag("parte/control/form_controls.html")
def parte_form_field_control(parte: ParteProducto) -> dict:
    return {"parte": parte}
