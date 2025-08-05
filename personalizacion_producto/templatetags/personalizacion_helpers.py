import os
import xml.etree.ElementTree as ET
import re, cairosvg, base64

from os import path
from django import template
from django.utils.safestring import SafeString
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_detail_line_for_personalizacion(personalizacion, pkcampo):
    return personalizacion.get_detail_by_field_pk(pkcampo)


@register.simple_tag
def get_value_for_personalizacion(personalizacion, pkcampo):
    return get_detail_line_for_personalizacion(personalizacion, pkcampo).valor


@register.simple_tag
def get_value_for_personalizacion_color(personalizacion, pkcampo):
    valor = get_detail_line_for_personalizacion(personalizacion, pkcampo).valor
    try:
        return valor.split("||")[2]
    except:
        return valor

@register.simple_tag
def procesa_svg(personalizacion):
    svg_content = ET.ElementTree(ET.fromstring(
        personalizacion.producto.svg_content)).getroot()
    for detalle in personalizacion.detalle.all():
        if detalle.campo.id_svg:
            elemento = svg_content.find(f".//*[@id='{detalle.campo.id_svg}']")
            valores_color = detalle.valor.split("||")
            elemento.set("fill", valores_color[0])
            print(f"{detalle.campo.id_svg =}")
            print(f"{elemento =}")
            print(f"{elemento.get('fill') =}")
            print(f"{valores_color =}")
            style_att = elemento.get("style")
            if style_att:
                style_rules = style_att.split(";")
                for idx,style_rule in enumerate(style_rules):
                    if "fill:" in style_rule:
                        style_rules[idx] = f"fill: {valores_color[0]}"
                elemento.set("style", ";".join(style_rules))
                print(f"{style_rules =}")
    final_content = ET.tostring(svg_content, encoding="unicode")

    imgpath = path.join(settings.MEDIA_ROOT, 'tmp', path.dirname(str(personalizacion.producto.imagen)))
    tmp_svg = path.join(imgpath, path.basename(str(personalizacion.producto.imagen)))
    tmp_png = tmp_svg + ".png"
    if not path.exists(imgpath):
        os.makedirs(imgpath)
    with open(tmp_svg, "w") as f:
        f.write(final_content)
    cairosvg.svg2png(url=tmp_svg, write_to=tmp_png)
    with open(tmp_png, "rb") as f:
        tmp_png_content = base64.b64encode(f.read()).decode("utf-8")
    return SafeString(f"""<img src="data:image/png;base64, {tmp_png_content}" style="width: 100%" />""")
    
    final_content = re.sub(r':?ns\d+:?', "", final_content)
    return SafeString(final_content)

@register.simple_tag
def get_svg_styles(personalizacion):
    return SafeString(personalizacion.get_styles())
