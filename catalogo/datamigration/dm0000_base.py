from catalogo.models import TipoParte
from catalogo.tipocampo.models import TipoCampo
from igs_app_base.menu.models import MenuOpc
from igs_app_base.models import App
from igs_app_base.utils.utils import add_or_create_menuopc


def migration():
    app = App.get_by_name("catalogo")
    gral = MenuOpc.objects.get(nombre="Generales", padre=app.menuopc)
    add_or_create_menuopc(
        "Tipos de Partes", 11,
        gral, "tipoparte")
    add_or_create_menuopc(
        "Tipos de Campos", 12,
        gral, "tipocampo")
    add_or_create_menuopc(
        "Tipos de Materiales", 1,
        app.menuopc, "tipomaterial")
    add_or_create_menuopc(
        "Tipos de Colores", 2,
        app.menuopc, "tipocolor")
    add_or_create_menuopc(
        "Categorías de Productos", 3,
        app.menuopc, "categoriaproducto")

    TipoParte.objects.get_or_create(tipo_de_parte="Estructura")
    TipoParte.objects.get_or_create(tipo_de_parte="Acabado")
    TipoParte.objects.get_or_create(tipo_de_parte="Tejido")

    TipoCampo.objects.get_or_create(
        tipo_de_campo="Tipo Material", tipo_interno="CAT_MATERIAL")
    TipoCampo.objects.get_or_create(
        tipo_de_campo="Tipo Color", tipo_interno="CAT_COLOR")
    TipoCampo.objects.get_or_create(
        tipo_de_campo="Color Abierto", tipo_interno="COLOR")
    TipoCampo.objects.get_or_create(
        tipo_de_campo="Campo Abierto", tipo_interno="ABIERTO")
