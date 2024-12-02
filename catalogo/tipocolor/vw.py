from typing import Any

from igs_app_base.views import GenericReadSuperCatalog
from igs_app_base.views import GenericViews

from .forms import MainForm
from .forms import OpcionColorForm
from .models import OpcionColor
from .models import TipoColor

views = GenericViews(
    TipoColor, "Tipo de Color", "Tipos de Color",
    "catalogo", MainForm, MainForm, MainForm)


class Read(GenericReadSuperCatalog):
    model = TipoColor
    titulo = "Tipo de Color"
    app = "catalogo"
    form_class = MainForm
    form_class_opcion = OpcionColorForm
    model_opcion = OpcionColor

    def create_opcion(self, post: Any):
        color = post.get("color")
        nombre = post.get("nombre")
        if color:
            self.model_opcion.objects.create(
                nombre=nombre,
                color=color,
                tipo_color=self.get_object())

    def update_opcion(self, post: Any):
        color = post.get("color")
        nombre = post.get("nombre")
        extra = post.get("extra")
        if color and extra:
            opc = self.model_opcion.objects.get(pk=int(extra))
            opc.color = color
            opc.nombre = nombre
            opc.save()


views.Read = Read
