from catalogo.models import TipoCampo

def migration():
    opc = TipoCampo.objects.get(tipo_interno='CAT_MATERIAL')
    opc.tipo_interno = 'CAT_OPCIONES'
    opc.tipo_de_campo = 'Catálogo de Opciones'
    opc.save()
