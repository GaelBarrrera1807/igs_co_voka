from igs_app_base.views import GenericViews, GenericCreate

from .forms import MainForm
from .models import EstadoPersonalizacion

views = GenericViews(
    EstadoPersonalizacion,
    "Estado de Personalizacion", "Estados de Personalizacion",
    "catalogo", MainForm, MainForm, MainForm)
