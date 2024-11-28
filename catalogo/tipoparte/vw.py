from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import TipoParte

views = GenericViews(
    TipoParte, "Tipo de Parte", "Tipos de Parte",
    "catalogo", MainForm, MainForm, MainForm)
