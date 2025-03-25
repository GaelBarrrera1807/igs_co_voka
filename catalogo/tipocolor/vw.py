from typing import Any

from igs_app_base.views import GenericReadSuperCatalog
from igs_app_base.views import GenericViews

from .forms import MainForm
from .forms import OpcionColorForm
from .models import OpcionColor
from .models import TipoColor

views = GenericViews(
    TipoColor, "Paleta de Colores", "Paletas de Colores",
    "catalogo", MainForm, MainForm, MainForm)


class Read(GenericReadSuperCatalog):
    model = TipoColor
    titulo = "Paleta de Colores"
    app = "catalogo"
    form_class = MainForm
    form_class_opcion = OpcionColorForm
    model_opcion = OpcionColor

    def create_opcion(self, post: Any, files: Any):
        color = post.get("color")
        if color:
            frm = OpcionColorForm(data=post, files=files)
            opc = frm.save(commit=False)
            opc.tipo_color=self.get_object()
            opc.save()

    def update_opcion(self, post: Any, files: Any):
        color = post.get("color")
        extra = post.get("extra")
        if color and extra:
            opc = self.model_opcion.objects.get(pk=int(extra))
            frm = OpcionColorForm(data=post, instance=opc, files=files)
            frm.save()


views.Read = Read
