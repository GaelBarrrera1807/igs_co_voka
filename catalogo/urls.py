from django.urls import include
from django.urls import path

urlpatterns = [
    path('tipo-de-parte/', include('catalogo.tipoparte.urls')),
    path('paleta-de-color/', include('catalogo.tipocolor.urls')),
    path('catalogo-de-opciones/', include('catalogo.tipomaterial.urls')),
    path(
        'categoria-de-productos/',
        include('catalogo.categoriaproducto.urls')),
    path('tipo-de-campo/', include('catalogo.tipocampo.urls')),
    path('estado-de-personalizacion/', include('catalogo.estadopersonalizacion.urls')),
    ]
