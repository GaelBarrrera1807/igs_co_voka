from django.contrib.auth.models import User
from django.db import models

from catalogo.models import EstadoPersonalizacion
from producto.models import CampoParteProducto
from producto.models import Producto


class Personalizacion(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    notas_y_comentarios = models.TextField(blank=True)
    producto = models.ForeignKey(
        Producto, models.PROTECT, "personalizaciones")
    user = models.ForeignKey(
        User, models.PROTECT, "personalizaciones", blank=True, null=True)
    estado = models.ForeignKey(EstadoPersonalizacion, models.PROTECT)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['estado__estado', 'actualizacion']

    def __str__(self):
        return f"{self.nombre} - {self.producto}"

    def get_detail_by_field_pk(self, pk: int) -> "PersonalizacionDetalle":
        for detail in self.detalle.all():
            if detail.campo.pk == pk:
                return detail
        return None

    def get_styles(self, pre_selector="#producto-svg "):
        css_rules = list()
        for pt in self.producto.partes.all():
            for campo in pt.campos.all():
                if campo.tipo_de_campo.tipo_interno == "CAT_COLOR":
                    selector = f"{pre_selector} #{campo.id_svg}".strip()
                    css_rules.append(f"{selector}{{fill: {self.get_detail_by_field_pk(campo.pk).valor.split('||')[0]};}}")
            for gpo in pt.gruposdecampos.all():
                for campo in gpo.campos.all():
                    if campo.tipo_de_campo.tipo_interno == "CAT_COLOR":
                        selector = f"{pre_selector} #{campo.id_svg}".strip()
                        css_rules.append(f"{selector}{{fill: {self.get_detail_by_field_pk(campo.pk).valor.split('||')[0]};}}")
        return "\n".join(css_rules)

class PersonalizacionDetalle(models.Model):
    personalizacion = models.ForeignKey(Personalizacion, models.CASCADE, "detalle")
    campo = models.ForeignKey(CampoParteProducto, models.PROTECT, related_name="personalizaciones")
    valor = models.TextField(blank=True, default="")

    class Meta:
        ordering = ['personalizacion', 'campo', 'valor']

    def __str__(self):
        return str(self.campo)
