from django.db import models


class TipoParte(models.Model):
    tipo_de_parte = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo_de_parte
