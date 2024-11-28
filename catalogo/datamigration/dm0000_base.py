from catalogo.models import TipoParte
from igs_app_base.models import App
from igs_app_base.utils.utils import add_or_create_menuopc


def migration():
    app = App.get_by_name("catalogo")
    add_or_create_menuopc(
        "Tipos de Partes", 1,
        app.menuopc, "tipoparte")
    add_or_create_menuopc(
        "Tipos de Materiales", 2,
        app.menuopc, "tipomaterial")
    add_or_create_menuopc(
        "Tipos de Colores", 3,
        app.menuopc, "tipocolor")
    add_or_create_menuopc(
        "Categorías de Productos", 4,
        app.menuopc, "categoriaproducto")

    TipoParte.objects.get_or_create(tipo_de_parte="Estructura")
    TipoParte.objects.get_or_create(tipo_de_parte="Acabado")
    TipoParte.objects.get_or_create(tipo_de_parte="Tejido")
