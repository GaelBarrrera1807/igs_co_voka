from django.db import models


class TipoCampo(models.Model):
    tipo_de_campo = models.CharField(max_length=200)
    tipo_interno = models.CharField(max_length=100)

    class Meta:
        ordering = ['tipo_de_campo', 'tipo_interno']

    def __str__(self):
        return self.tipo_de_campo
