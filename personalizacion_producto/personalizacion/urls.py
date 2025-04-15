from django.urls import path

from .vw import views, CreateFromUser

obj = 'personalizacion'
app_label = 'personalizacion_producto'

urlpatterns = views.create_urls(app_label) + [
    path('enviar-personalizacion/', CreateFromUser.as_view(), name="enviar_personalizacion")
]
