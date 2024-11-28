from igs_app_base.hiperforms import BaseHiperModelForm

from .models import CategoriaProducto


class MainForm(BaseHiperModelForm):
    class Meta:
        model = CategoriaProducto
        fields = "__all__"
