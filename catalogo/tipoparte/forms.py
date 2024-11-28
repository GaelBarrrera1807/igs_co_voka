from igs_app_base.hiperforms import BaseHiperModelForm

from .models import TipoParte


class MainForm(BaseHiperModelForm):
    class Meta:
        model = TipoParte
        fields = "__all__"
