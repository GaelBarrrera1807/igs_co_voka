from django.urls import include
from django.urls import path

urlpatterns = [
    path(
        'personalizacion-de-producto/',
        include('personalizacion_producto.personalizacion.urls')),
    ]
