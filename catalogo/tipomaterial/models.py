from django.db import models


class TipoMaterial(models.Model):
    tipo_de_material = models.CharField(max_length=200)

    class Meta:
        ordering = ['tipo_de_material']

    def __str__(self):
        return self.tipo_de_material


class OpcionMaterial(models.Model):
    material = models.CharField(max_length=50)
    tipo_material = models.ForeignKey(
        TipoMaterial, models.CASCADE, "opciones")

    class Meta:
        ordering = ['material']

    def __str__(self):
        return self.material
