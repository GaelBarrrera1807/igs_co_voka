from django import forms

from igs_app_base.hiperforms import BaseHiperModelForm

from .models import CampoParteProducto
from .models import GrupoCampos
from .models import ParteProducto


class MainFormParte(BaseHiperModelForm):

    class Meta:
        model = ParteProducto
        fields = ["nombre", "posicion", "tipo_de_parte", "paletas_de_color", ]
        widgets = {"paletas_de_color": forms.CheckboxSelectMultiple()}


class MainFormCampo(BaseHiperModelForm):

    class Meta:
        model = CampoParteProducto
        fields = [
            "nombre", "posicion", "id_svg",
            "tipo_de_campo",
            "opciones_material" ]
        widgets = {"id_svg": forms.TextInput(attrs={"list": "svp_option_id"})}

class MainFormGrupo(BaseHiperModelForm):

    class Meta:
        model = GrupoCampos
        fields = [
            "nombre", "posicion" ]
