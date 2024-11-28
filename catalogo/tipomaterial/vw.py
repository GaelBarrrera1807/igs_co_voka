from typing import Any

from igs_app_base.views import GenericReadSuperCatalog
from igs_app_base.views import GenericViews

from .forms import MainForm
from .forms import OpcionMaterialForm
from .models import OpcionMaterial
from .models import TipoMaterial

views = GenericViews(
    TipoMaterial, "Tipo de Material", "Tipos de Material",
    "catalogo", MainForm, MainForm, MainForm)


class Read(GenericReadSuperCatalog):
    model = TipoMaterial
    titulo = "Tipo de Material"
    app = "catalogo"
    form_class = MainForm
    form_class_opcion = OpcionMaterialForm
    model_opcion = OpcionMaterial

    def create_opcion(self, post: Any):
        material = post.get("material")
        if material:
            self.model_opcion.objects.create(
                material=material,
                tipo_material=self.get_object())

    def update_opcion(self, post: Any):
        material = post.get("material")
        extra = post.get("extra")
        if material and extra:
            opc = self.model_opcion.objects.get(pk=int(extra))
            opc.material = material
            opc.save()


views.Read = Read
