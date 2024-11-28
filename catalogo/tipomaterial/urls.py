from .vw import views

obj = 'tipomaterial'
app_label = 'voka_catalogo'

urlpatterns = views.create_urls(app_label)
