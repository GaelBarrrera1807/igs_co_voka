from django import forms

from igs_app_base.hiperforms import BaseHiperModelForm

from .models import Producto


class MainForm(BaseHiperModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {'categorias': forms.CheckboxSelectMultiple()}
