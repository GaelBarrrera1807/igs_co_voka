from igs_app_base.views import GenericCreate
from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import EstadoPersonalizacion

views = GenericViews(
    EstadoPersonalizacion,
    "Estado de Personalizacion", "Estados de Personalizacion",
    "catalogo", MainForm, MainForm, MainForm)
