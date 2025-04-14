from igs_app_base.models import MenuOpc

def migration():
    mnuopc = MenuOpc.objects.get(
        nombre="Tipos de Materiales", vista="tipomaterial_list")
    mnuopc.nombre = "Catálogos de Opciones"
    mnuopc.save()
