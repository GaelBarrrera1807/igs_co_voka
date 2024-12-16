from igs_app_base.hiperforms import BaseHiperModelForm

from .models import EstadoPersonalizacion


class MainForm(BaseHiperModelForm):
    class Meta:
        model = EstadoPersonalizacion
        fields = "__all__"
