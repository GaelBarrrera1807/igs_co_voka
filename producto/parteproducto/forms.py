from django import forms

from igs_app_base.hiperforms import BaseHiperModelForm

from .models import CampoParteProducto
from .models import ParteProducto


class MainFormParte(BaseHiperModelForm):

    class Meta:
        model = ParteProducto
        fields = ["nombre", "posicion", "tipo_de_parte", ]


class MainFormCampo(BaseHiperModelForm):

    class Meta:
        model = CampoParteProducto
        fields = [
            "nombre", "posicion", "id_svg",
            "tipo_de_campo",
            "opciones_material", "opciones_color", ]
        widgets = {"id_svg": forms.TextInput(attrs={"list": "svp_option_id"})}
