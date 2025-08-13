from catalogo.estadopersonalizacion.models import EstadoPersonalizacion
from igs_app_base.models import App
from igs_app_base.models import MenuOpc
from igs_app_base.utils.utils import add_or_create_menuopc


def migration():
    app = App.get_by_name("catalogo")
    gral = MenuOpc.objects.get(nombre="Generales", padre=app.menuopc)
    add_or_create_menuopc(
        "Estados de Personalizaciones", 13,
        gral, "estadopersonalizacion")

    EstadoPersonalizacion.objects.get_or_create(
        estado="Iniciado", estado_interno="STARTED")
    EstadoPersonalizacion.objects.get_or_create(
        estado="Pausado", estado_interno="STAND BY")
    EstadoPersonalizacion.objects.get_or_create(
        estado="Terminado", estado_interno="FINISHED")
    EstadoPersonalizacion.objects.get_or_create(
        estado="En Fabricación", estado_interno="MANUFACTURING")
    EstadoPersonalizacion.objects.get_or_create(
        estado="Listo para Envío", estado_interno="READY2SEND")
    EstadoPersonalizacion.objects.get_or_create(
        estado="Enviado", estado_interno="SENT")
    EstadoPersonalizacion.objects.get_or_create(
        estado="Cancelado", estado_interno="CANCELED")
