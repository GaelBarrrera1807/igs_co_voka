from igs_app_base.hiperforms import BaseHiperModelForm

from .models import OpcionMaterial
from .models import TipoMaterial


class MainForm(BaseHiperModelForm):
    class Meta:
        model = TipoMaterial
        fields = "__all__"


class OpcionMaterialForm(BaseHiperModelForm):
    class Meta:
        model = OpcionMaterial
        fields = ['orden', 'material', 'imagen']
