from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path

from .views import ProductoView

urlpatterns = [
    path('producto/', include('producto.producto.urls')),
    path(
        'productos',
        login_required()(ProductoView.as_view()),
        name="idx_app_producto"),
]
