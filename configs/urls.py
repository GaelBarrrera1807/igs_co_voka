"""
URL configuration for configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from producto.views import DisclaimerProds
from producto.views import DisplayOpenProds

urlpatterns = ([
    path('admin/', admin.site.urls),

    # PATCH urls for productos display
    path("", DisclaimerProds.as_view(), name="session_imin_disclaimer"),
    path("nuestros-produtos/", DisplayOpenProds.as_view(), name="display_open_products"),
    path('', include('igs_app_base.urls')),
    path('', include('igs_app_catalogo.urls')),
    path('', include('igs_app_favorito.urls')),
    path('', include('catalogo.urls')),
    path('', include('producto.urls')),
    path('', include('personalizacion_producto.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
