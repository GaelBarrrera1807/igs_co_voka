from typing import Any

from igs_app_base.views import GenericReadSuperCatalog
from igs_app_base.views import GenericViews

from .forms import MainForm
from .forms import OpcionMaterialForm
from .models import OpcionMaterial
from .models import TipoMaterial

views = GenericViews(
    TipoMaterial, "Catálogo de Opciones", "Catálogos de Opciones",
    "catalogo", MainForm, MainForm, MainForm)


class Read(GenericReadSuperCatalog):
    model = TipoMaterial
    titulo = "Catálogo de Opciones"
    app = "catalogo"
    form_class = MainForm
    form_class_opcion = OpcionMaterialForm
    model_opcion = OpcionMaterial

    def create_opcion(self, post: Any, files: Any):
        material = post.get("material")
        if material:
            frm = OpcionMaterialForm(data=post, files =files)
            opc = frm.save(commit=False)
            opc.tipo_material = self.get_object()
            opc.save()

    def update_opcion(self, post: Any, files: Any):
        material = post.get("material")
        extra = post.get("extra")
        if material and extra:
            opc = self.model_opcion.objects.get(pk=int(extra))
            frm = OpcionMaterialForm(data=post, files =files, instance=opc)
            frm.save()


views.Read = Read
