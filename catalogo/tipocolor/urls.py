from .vw import views

obj = 'tipocolor'
app_label = 'catalogo'

urlpatterns = views.create_urls(app_label)
