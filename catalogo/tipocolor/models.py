from django.db import models


class TipoColor(models.Model):
    tipo_de_color = models.CharField(max_length=200)

    class Meta:
        ordering = ['tipo_de_color']

    def __str__(self):
        return self.tipo_de_color


class OpcionColor(models.Model):
    color = models.CharField(max_length=50)
    tipo_color = models.ForeignKey(
        TipoColor, models.CASCADE, "opciones")

    class Meta:
        ordering = ['color']

    def __str__(self):
        return self.color
