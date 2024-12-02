from igs_app_base.models import App
from igs_app_base.utils.utils import add_or_create_menuopc


def migration():
    app, created = App.objects.get_or_create(nombre="producto")
    if created:
        app.posicion = 1
        app.save()

    prod = add_or_create_menuopc(
        "Producto", 1,
        None, None, None, "idx_app_producto")
    add_or_create_menuopc(
        "Productos", 1, prod, "producto")
