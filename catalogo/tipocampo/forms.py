from igs_app_base.hiperforms import BaseHiperModelForm

from .models import TipoCampo


class MainForm(BaseHiperModelForm):
    class Meta:
        model = TipoCampo
        fields = "__all__"
