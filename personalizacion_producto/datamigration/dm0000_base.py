from igs_app_base.models import App
from igs_app_base.utils.utils import add_or_create_menuopc


def migration():
    app = App.objects.get(nombre="producto")

    add_or_create_menuopc(
        "Personalizaciones de Productos", 2, app.menuopc,
        "personalizacion")
