from .vw import views

obj = 'tipoparte'
app_label = 'catalogo'

urlpatterns = views.create_urls(app_label)
