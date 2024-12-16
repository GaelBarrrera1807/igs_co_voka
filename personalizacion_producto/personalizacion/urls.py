from .vw import views

obj = 'personalizacion'
app_label = 'personalizacion_producto'

urlpatterns = views.create_urls(app_label)
