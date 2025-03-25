from igs_app_base.models import MenuOpc

def migration():
    mnuopc = MenuOpc.objects.get(
        nombre="Tipos de Colores", vista="tipocolor_list")
    mnuopc.nombre = "Paletas de Colores"
    mnuopc.save()
