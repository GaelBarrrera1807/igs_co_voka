from http.client import HTTPResponse
from io import BytesIO

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django_weasyprint import WeasyTemplateResponseMixin
from weasyprint import HTML
from xhtml2pdf import pisa

import json

from igs_app_base.views import GenericViews, GenericCreate, GenericRead
from producto.models import Producto
from catalogo.models import EstadoPersonalizacion

from .forms import MainForm
from .models import Personalizacion, PersonalizacionDetalle

views = GenericViews(
    Personalizacion, "Personalización", "Personalizaciones",
    "producto", MainForm, MainForm, MainForm)

def create_empty_personalizacion(
        nombre: str, telefono: str, correo_electronico: str,
        notas_y_comentarios: str, producto: int, user: int
        ) -> Personalizacion:
    producto = Producto.objects.get(pk=producto)
    user = User.objects.get(pk=user) if user > 0 else None
    estado = EstadoPersonalizacion.objects.get(estado_interno="STARTED")
    personalizacion = Personalizacion.objects.create(
        nombre=nombre, telefono=telefono, correo_electronico=correo_electronico,
        notas_y_comentarios=notas_y_comentarios, producto=producto, user=user,
        estado=estado)
    for parte in personalizacion.producto.partes.all():
        for campo in parte.campos.all():
            PersonalizacionDetalle.objects.create(
                personalizacion=personalizacion, campo=campo)
        for gpo in parte.gruposdecampos.all():
            for campo in gpo.campos.all():
                PersonalizacionDetalle.objects.create(
                    personalizacion=personalizacion, campo=campo)
    return personalizacion

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

class CreateFromUser(TemplateView):
    def post(self, request, *args, **kwargs):
        producto_pk = int(request.POST.get('producto_pk', '0'))
        pk = 0
        if producto_pk > 0:
            user = request.POST.get('user_pk', "")
            user = int(user) if user != "None" else 0
            personalizacion = create_empty_personalizacion(
                request.POST.get('user_nombre', ""),
                request.POST.get('user_telefono', ""),
                request.POST.get('user_correo', ""),
                request.POST.get('user_notas', ""),
                producto_pk,
                user
            )
            pk = personalizacion.pk
            campos_color = json.loads(request.POST.get('campos_color', '{}',))
            for campo_valor in personalizacion.detalle.all():
                if campo_valor.campo.tipo_de_campo.tipo_interno == "CAT_COLOR":
                    campo_valor.valor = campos_color[f"campo-{campo_valor.campo.pk}"]
                else:
                    campo_valor.valor = request.POST.get(f"campo-{campo_valor.campo.pk}", '')
                campo_valor.save()
        return HttpResponseRedirect(reverse('ver_personalizacion', kwargs={'pk': pk}))


class ViewPersonalizacion(GenericRead):
    template_name = "personalizacion_producto/create_from_user.html"
    model = Personalizacion
    form_class = MainForm


def ViewPDFPersonalizacion(request, pk):
    object = Personalizacion.objects.get(pk=pk)
    html = str(render_to_string("personalizacion_producto/create_from_user.html", {
        'object': object
    }) + "")
    # response = HttpResponse(content_type="application/pdf")
    # response["Content-Disposition"] = f'attachment; filename="Personalizacion {object.producto}.pdf"'
    # HTML(string=html).write_pdf(response)
    result = pisa.CreatePDF(html, dest=BytesIO())
    if result.err:
        return HttpResponse('Error generating PDF: %s' % result.err)
    response = HttpResponse(content_type='application/pdf')
    response.write(result.dest.getvalue())
    return response
