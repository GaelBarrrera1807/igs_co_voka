from django import template

register = template.Library()


@register.simple_tag
def get_detail_line_for_personalizacion(personalizacion, pkcampo):
    return personalizacion.get_detail_by_field_pk(pkcampo)


@register.simple_tag
def get_value_for_personalizacion(personalizacion, pkcampo):
    return get_detail_line_for_personalizacion(personalizacion, pkcampo).valor
