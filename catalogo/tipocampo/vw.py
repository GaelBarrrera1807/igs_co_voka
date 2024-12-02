from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import TipoCampo

views = GenericViews(
    TipoCampo, "Tipo de Campo", "Tipos de Campo",
    "catalogo", MainForm, MainForm, MainForm)
