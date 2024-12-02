from catalogo.models import CategoriaProducto
from catalogo.models import TipoCampo
from catalogo.models import TipoColor
from catalogo.models import TipoMaterial
from catalogo.models import TipoParte
from producto.models import CampoParteProducto
from producto.models import ParteProducto
from producto.models import Producto


def migration():
    banca, created = Producto.objects.get_or_create(nombre="(Ejemplo) Banca")
    if created:
        banca.categorias.add(
            CategoriaProducto.objects.get_or_create(
                categoria="(Ejemplo) Bancas")[0])
        banca.categorias.add(
            CategoriaProducto.objects.get_or_create(
                categoria="(Ejemplo) Metalicas")[0])
        banca.save()

        parte = ParteProducto.objects.create(
            nombre="Estructura", producto=banca, posicion=1,
            tipo_de_parte=TipoParte.objects.get(tipo_de_parte="Estructura"))
        CampoParteProducto.objects.create(
            nombre="Tipo de Material", parte_producto=parte, posicion=1,
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_MATERIAL"),
            opciones_material=TipoMaterial.objects.get(
                tipo_de_material="(Ejemplo) Material Estructural"))
        CampoParteProducto.objects.create(
            nombre="Color", parte_producto=parte, posicion=2,
            id_svg="estructura",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))

        parte = ParteProducto.objects.create(
            nombre="Tejido", producto=banca, posicion=2,
            tipo_de_parte=TipoParte.objects.get(tipo_de_parte="Tejido"))
        CampoParteProducto.objects.create(
            nombre="Tejido 1", parte_producto=parte, posicion=1,
            id_svg="tejido1",
            tipo_de_campo=TipoCampo.objects.get(tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Tejido 2", parte_producto=parte, posicion=2,
            id_svg="tejido2",
            tipo_de_campo=TipoCampo.objects.get(tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Tejido 3", parte_producto=parte, posicion=3,
            id_svg="tejido3",
            tipo_de_campo=TipoCampo.objects.get(tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACR"))

        parte = ParteProducto.objects.create(
            nombre="Notas y Aclaraciones", producto=banca, posicion=3,
            tipo_de_parte=TipoParte.objects.get(tipo_de_parte="Acabado"))
        CampoParteProducto.objects.create(
            nombre="Largo", parte_producto=parte, posicion=1,
            tipo_de_campo=TipoCampo.objects.get(tipo_interno="ABIERTO"))
        CampoParteProducto.objects.create(
            nombre="Ancho", parte_producto=parte, posicion=2,
            tipo_de_campo=TipoCampo.objects.get(tipo_interno="ABIERTO"))
        CampoParteProducto.objects.create(
            nombre="Alto", parte_producto=parte, posicion=3,
            tipo_de_campo=TipoCampo.objects.get(tipo_interno="ABIERTO"))
        CampoParteProducto.objects.create(
            nombre="Notas y Comentarios", parte_producto=parte, posicion=4,
            tipo_de_campo=TipoCampo.objects.get(tipo_interno="ABIERTO"))

    cordon, created = Producto.objects.get_or_create(nombre="(Ejemplo Cordon")
    if created:
        cordon.categorias.add(
            CategoriaProducto.objects.get_or_create(
                categoria="(Ejemplo) Pasamaneria")[0])
        cordon.save()

        parte = ParteProducto.objects.create(
            nombre="Cabo 1", producto=cordon, posicion=1,
            tipo_de_parte=TipoParte.objects.get(tipo_de_parte="Tejido"))
        CampoParteProducto.objects.create(
            nombre="Hilo 1", parte_producto=parte, posicion=1,
            id_svg="C1Hilo1",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Hilo 2", parte_producto=parte, posicion=2,
            id_svg="C1Hilo2",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Hilo 3", parte_producto=parte, posicion=3,
            id_svg="C1Hilo3",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Hilo 4", parte_producto=parte, posicion=4,
            id_svg="C1Hilo4",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Hilo 5", parte_producto=parte, posicion=5,
            id_svg="C1Hilo5",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Hilo 6", parte_producto=parte, posicion=6,
            id_svg="C1Hilo6",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Hilo 7", parte_producto=parte, posicion=7,
            id_svg="C1Hilo7",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))
        CampoParteProducto.objects.create(
            nombre="Hilo 8", parte_producto=parte, posicion=8,
            id_svg="C1Hilo8",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) ACE"))

        parte = ParteProducto.objects.create(
            nombre="Cabo 2", producto=cordon, posicion=2,
            tipo_de_parte=TipoParte.objects.get(tipo_de_parte="Tejido"))
        CampoParteProducto.objects.create(
            nombre="Hilo 1", parte_producto=parte, posicion=1,
            id_svg="C2Hilo1",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Madera"))
        CampoParteProducto.objects.create(
            nombre="Hilo 2", parte_producto=parte, posicion=2,
            id_svg="C2Hilo2",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Madera"))
        CampoParteProducto.objects.create(
            nombre="Hilo 3", parte_producto=parte, posicion=3,
            id_svg="C2Hilo3",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Madera"))
        CampoParteProducto.objects.create(
            nombre="Hilo 4", parte_producto=parte, posicion=4,
            id_svg="C2Hilo4",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Madera"))
        CampoParteProducto.objects.create(
            nombre="Hilo 5", parte_producto=parte, posicion=5,
            id_svg="C2Hilo5",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Madera"))
        CampoParteProducto.objects.create(
            nombre="Hilo 6", parte_producto=parte, posicion=6,
            id_svg="C2Hilo6",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Madera"))
        CampoParteProducto.objects.create(
            nombre="Hilo 7", parte_producto=parte, posicion=7,
            id_svg="C2Hilo7",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Madera"))
        CampoParteProducto.objects.create(
            nombre="Hilo 8", parte_producto=parte, posicion=8,
            id_svg="C2Hilo8",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Madera"))

        parte = ParteProducto.objects.create(
            nombre="Cabo 3", producto=cordon, posicion=3,
            tipo_de_parte=TipoParte.objects.get(tipo_de_parte="Tejido"))
        CampoParteProducto.objects.create(
            nombre="Hilo 1", parte_producto=parte, posicion=1,
            id_svg="C3Hilo1",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))
        CampoParteProducto.objects.create(
            nombre="Hilo 2", parte_producto=parte, posicion=2,
            id_svg="C3Hilo2",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))
        CampoParteProducto.objects.create(
            nombre="Hilo 3", parte_producto=parte, posicion=3,
            id_svg="C3Hilo3",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))
        CampoParteProducto.objects.create(
            nombre="Hilo 4", parte_producto=parte, posicion=4,
            id_svg="C3Hilo4",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))
        CampoParteProducto.objects.create(
            nombre="Hilo 5", parte_producto=parte, posicion=5,
            id_svg="C3Hilo5",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))
        CampoParteProducto.objects.create(
            nombre="Hilo 6", parte_producto=parte, posicion=6,
            id_svg="C3Hilo6",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))
        CampoParteProducto.objects.create(
            nombre="Hilo 7", parte_producto=parte, posicion=7,
            id_svg="C3Hilo7",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))
        CampoParteProducto.objects.create(
            nombre="Hilo 8", parte_producto=parte, posicion=8,
            id_svg="C3Hilo8",
            tipo_de_campo=TipoCampo.objects.get(
                tipo_interno="CAT_COLOR"),
            opciones_color=TipoColor.objects.get(
                tipo_de_color="(Ejemplo) Metal"))
