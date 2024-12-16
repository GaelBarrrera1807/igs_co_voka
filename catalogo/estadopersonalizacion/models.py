from django.db import models


class EstadoPersonalizacion(models.Model):
    estado = models.CharField(max_length=200)
    estado_interno = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ['estado', 'estado_interno']

    def __str__(self):
        return self.estado
