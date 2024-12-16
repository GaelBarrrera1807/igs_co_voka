import random as rn

from catalogo.models import CategoriaProducto
from catalogo.models import TipoCampo
from catalogo.models import TipoColor
from catalogo.models import TipoMaterial
from catalogo.models import TipoParte
from producto.models import CampoParteProducto
from producto.models import ParteProducto
from producto.models import Producto


def add_parte(prod):
    parte = ParteProducto.objects.create(
        nombre="Notas y Aclaraciones", producto=prod, posicion=1,
        tipo_de_parte=TipoParte.objects.get(tipo_de_parte="Acabado"))
    for idx, campo in enumerate(["Largo", "Ancho", "Alto", "Notas y Comentarios", ]):
        CampoParteProducto.objects.create(
            nombre=campo, parte_producto=parte, posicion=idx + 1,
            tipo_de_campo=TipoCampo.objects.get(tipo_interno="ABIERTO"))

def migration():
    nprods = rn.randint(10, 25)
    cats = list(CategoriaProducto.objects.all())
    for np in range(nprods):
        nombre = f"producto_{np + 1:03}"
        prod, cprod = Producto.objects.get_or_create(nombre=nombre, precio=0)
        if cprod:
            ncat = rn.randint(0, len(cats))
            prod.categorias.set(rn.sample(cats, ncat))
            add_parte(prod)

