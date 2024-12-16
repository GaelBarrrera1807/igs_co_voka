from http.client import HTTPResponse

from django.http import HttpResponseRedirect

from igs_app_base.views import GenericViews, GenericCreate, GenericRead

from .forms import MainForm
from .models import Personalizacion, PersonalizacionDetalle

views = GenericViews(
    Personalizacion, "Personalización", "Personalizaciones",
    "producto", MainForm, MainForm, MainForm)


class Create(GenericCreate):
    model = Personalizacion
    titulo = "Personalización"
    app = "producto"
    form_class = MainForm

    def form_valid(self, form):
        response = super().form_valid(form)
        for parte in self.object.producto.partes.all():
            for campo in parte.campos.all():
                PersonalizacionDetalle.objects.create(
                    personalizacion=self.object, campo=campo)
        return response


class Read(GenericRead):
    model = Personalizacion
    titulo = "Personalización"
    app = "producto"
    form_class = MainForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pkcampo = request.POST.get('pkcampo')
        valor = request.POST.get(f'campo-html-object-{pkcampo}')
        action = request.POST.get('action')
        if action == "update-field-value":
            detail = self.object.get_detail_by_field_pk(int(pkcampo))
            if detail:
                detail.valor = valor
                detail.save()
        return HttpResponseRedirect(request.path)

views.Create = Create
views.Read = Read
