from .vw import views

obj = 'estadopersonalizacion'
app_label = 'catalogo'

urlpatterns = views.create_urls(app_label)
