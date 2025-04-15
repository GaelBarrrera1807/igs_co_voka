from django.db import models
from django.utils.safestring import SafeString

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
    paletas_de_color = models.ManyToManyField(
        TipoColor, blank=True)

    class Meta:
        ordering = ["posicion", "nombre"]

    def __str__(self):
        return self.nombre

    @property
    def detalle(self) -> list:
        elementos = list(self.campos.all()) + list(self.gruposdecampos.all())
        elementos.sort(
            key=lambda item: f"{item.posicion:09} - {item.nombre.upper()}")
        return elementos

    @property
    def has_color_palette_fields(self) -> bool:
        tcpc = TipoCampo.objects.get(tipo_interno__iexact="CAT_COLOR")
        res = any([
            campo.tipo_de_campo.pk == tcpc.pk
            for campo in self.campos.all()
        ])
        if res:
            return res
        return any([
            gpo.has_color_palette_fields
            for gpo in self.gruposdecampos.all()
        ])


class GrupoCampos(models.Model):
    nombre = models.CharField(max_length=200)
    posicion = models.PositiveSmallIntegerField(
        help_text="Orden del grupo de campos en que se realizará "
                  "la personalización del producto")
    parte_producto = models.ForeignKey(
        ParteProducto, models.CASCADE, "gruposdecampos")
    class Meta:
        ordering = ['posicion', "nombre"]

    def __str__(self):
        return self.nombre

    @property
    def has_color_palette_fields(self) -> bool:
        tcpc = TipoCampo.objects.get(tipo_interno__iexact="CAT_COLOR")
        return any([
            campo.tipo_de_campo.pk == tcpc.pk
            for campo in self.campos.all()
        ])

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
        ParteProducto, models.CASCADE, "campos",
        null=True, blank=True)
    grupo_producto = models.ForeignKey(
        GrupoCampos, models.CASCADE, "campos",
        null=True, blank=True)
    tipo_de_campo = models.ForeignKey(TipoCampo, models.PROTECT)
    opciones_material = models.ForeignKey(
        TipoMaterial, models.PROTECT, blank=True, null=True, verbose_name="Catálogo de Opciones")

    class Meta:
        ordering = ['posicion', "nombre"]

    def __str__(self):
        return self.nombre

