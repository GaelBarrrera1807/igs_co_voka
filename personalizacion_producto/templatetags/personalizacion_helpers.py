from django import template
from django.utils.safestring import SafeString
import xml.etree.ElementTree as ET
import re

register = template.Library()


@register.simple_tag
def get_detail_line_for_personalizacion(personalizacion, pkcampo):
    return personalizacion.get_detail_by_field_pk(pkcampo)


@register.simple_tag
def get_value_for_personalizacion(personalizacion, pkcampo):
    return get_detail_line_for_personalizacion(personalizacion, pkcampo).valor

@register.simple_tag
def procesa_svg(personalizacion):
    svg_content = ET.ElementTree(ET.fromstring(
        personalizacion.producto.svg_content)).getroot()
    for detalle in personalizacion.detalle.all():
        if detalle.campo.id_svg:
            elemento = svg_content.find(f".//*[@id='{detalle.campo.id_svg}']")
            valores_color = detalle.valor.split("||")
            elemento.set("fill", valores_color[0])
    final_content = ET.tostring(svg_content, encoding="unicode")
    final_content = re.sub(r':?ns\d+:?', "", final_content)
    return SafeString(final_content)
