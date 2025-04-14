from django.db import models


class TipoMaterial(models.Model):
    tipo_de_material = models.CharField(max_length=200, verbose_name="Catálogo")

    class Meta:
        ordering = ['tipo_de_material']

    def __str__(self):
        return self.tipo_de_material


class OpcionMaterial(models.Model):
    material = models.CharField(max_length=50, verbose_name="Opción")
    tipo_material = models.ForeignKey(
        TipoMaterial, models.CASCADE, "opciones", verbose_name="Catálogo")
    imagen = models.FileField(
        upload_to="opcioncatalogo", null=True, blank=True,
        help_text="Tamaño recomendado de 100x45")

    class Meta:
        ordering = ['material']

    def __str__(self):
        return self.material
