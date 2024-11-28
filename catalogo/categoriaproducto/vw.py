from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import CategoriaProducto

views = GenericViews(
    CategoriaProducto,
    "Categoría de Productos", "Categorías de Productos",
    "catalogo", MainForm, MainForm, MainForm)
