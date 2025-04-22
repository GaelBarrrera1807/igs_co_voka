from catalogo.models import TipoCampo
from igs_app_base.models import MenuOpc

def migration():
    mnuopc = MenuOpc.objects.get(
        nombre="Catálogos de Opciones", vista="tipomaterial_list")
    mnuopc.nombre = "Opciones de Productos"
    mnuopc.save()

    opc = TipoCampo.objects.get(tipo_interno='CAT_OPCIONES')
    opc.tipo_interno = 'OPCIONES_PRODUCTOS'
    opc.tipo_de_campo = 'Opciones de Productos'
    opc.save()
