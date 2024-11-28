from .vw import views

obj = 'categoriaproducto'
app_label = 'catalogo'

urlpatterns = views.create_urls(app_label)
