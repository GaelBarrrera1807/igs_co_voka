from .vw import views

obj = 'tipomaterial'
app_label = 'catalogo'

urlpatterns = views.create_urls(app_label)
