from .vw import views

obj = 'tipoparte'
app_label = 'voka_catalogo'

urlpatterns = views.create_urls(app_label)
