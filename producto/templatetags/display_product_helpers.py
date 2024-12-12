from django import template

from catalogo.models import CategoriaProducto
from producto.models import Producto

register = template.Library()

@register.inclusion_tag("producto/display/table.html", takes_context=True)
def display_product_table(context) -> dict:
    return {"products":
                list(Producto.objects.filter(mostrar_en_galeria=True)),
            "MEDIA_URL": context.get('MEDIA_URL')}


@register.inclusion_tag("producto/display/categories.html")
def display_product_categories_tree() -> dict:
    return {"categories":
                list(CategoriaProducto.objects.filter(categoria_padre=None))}

