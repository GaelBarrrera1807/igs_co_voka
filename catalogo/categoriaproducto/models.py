from django.db import models


class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=50)
    mostrar_en_landing_page = models.BooleanField(blank=True, default=True)
    categoria_padre = models.ForeignKey(
        "CategoriaProducto", models.CASCADE, "subcategorias",
        blank=True, null=True)

    class Meta:
        ordering = ['categoria']

    def __str__(self):
        return self.categoria
