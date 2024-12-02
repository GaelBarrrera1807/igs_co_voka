from django.db import models

from catalogo.models import TipoCampo
from catalogo.models import TipoParte
from catalogo.tipocolor.models import TipoColor
from catalogo.tipomaterial.models import TipoMaterial
from producto.models import Producto


class ParteProducto(models.Model):
    nombre = models.CharField(max_length=200)
    posicion = models.PositiveSmallIntegerField(
        help_text="Orden de la parte en que se realizará "
                  "la personalización del producto")
    producto = models.ForeignKey(
        Producto, models.CASCADE, "partes")
    tipo_de_parte = models.ForeignKey(TipoParte, models.PROTECT)

    class Meta:
        ordering = ["posicion", "nombre"]

    def __str__(self):
        return self.nombre


class CampoParteProducto(models.Model):
    nombre = models.CharField(max_length=200)
    posicion = models.PositiveSmallIntegerField(
        help_text="Orden del campo en que se realizará "
                  "la personalización del producto")
    id_svg = models.CharField(
        max_length=100, blank=True,
        help_text="ID del elemento de la svg correspondiente a la "
                  "personalización del producto")
    parte_producto = models.ForeignKey(
        ParteProducto, models.CASCADE, "campos")
    tipo_de_campo = models.ForeignKey(TipoCampo, models.PROTECT)
    opciones_material = models.ForeignKey(
        TipoMaterial, models.PROTECT, blank=True, null=True)
    opciones_color = models.ForeignKey(
        TipoColor, models.PROTECT, blank=True, null=True)

    class Meta:
        ordering = ['posicion', "nombre"]

    def __str__(self):
        return self.nombre
