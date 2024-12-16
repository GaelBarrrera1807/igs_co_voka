from igs_app_base.hiperforms import BaseHiperModelForm

from .models import Personalizacion


class MainForm(BaseHiperModelForm):
    class Meta:
        model = Personalizacion
        fields = "__all__"
