from catalogo.models import OpcionColor
from catalogo.models import OpcionMaterial
from catalogo.models import TipoColor
from catalogo.models import TipoMaterial, CategoriaProducto


def migration():
    cat = TipoColor.objects.get_or_create(tipo_de_color="(Ejemplo) ACE")[0]
    OpcionColor.objects.get_or_create(color="#d1c762", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#3a7f65", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#a6b2aa", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#b75b63", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#c93742", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#3b3e5f", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#70674f", tipo_color=cat)

    cat = TipoColor.objects.get_or_create(tipo_de_color="(Ejemplo) ACR")[0]
    OpcionColor.objects.get_or_create(color="#2190b1", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#806a9f", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#102675", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#ebb4b8", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#ee793e", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#359024", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#bf881f", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#0c0f10", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#5b2c30", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#6f6e5a", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#5f743a", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#1f3f97", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#987745", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#871119", tipo_color=cat)

    cat = TipoColor.objects.get_or_create(tipo_de_color="(Ejemplo) ASD")[0]
    OpcionColor.objects.get_or_create(color="#877228", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#862115", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#5c3126", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#24293c", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#202127", tipo_color=cat)

    cat = TipoColor.objects.get_or_create(tipo_de_color="(Ejemplo) Metal")[0]
    OpcionColor.objects.get_or_create(color="#cda87e", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#abb88c", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#a9a9a9", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#be8e99", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#97b19c", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#94b8b6", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#a09baf", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#b7a898", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#8ca2bc", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#bdb68a", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#b09995", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#cb8f77", tipo_color=cat)

    cat = TipoColor.objects.get_or_create(tipo_de_color="(Ejemplo) Madera")[0]
    OpcionColor.objects.get_or_create(color="#fad5a0", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#f9d79c", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#dfbe92", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#dfbe92", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#deac77", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#b7885f", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#9b582c", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#943d21", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#705246", tipo_color=cat)
    OpcionColor.objects.get_or_create(color="#85351a", tipo_color=cat)

    cat = TipoMaterial.objects.get_or_create(
        tipo_de_material="(Ejemplo) Material Estructural")[0]
    OpcionMaterial.objects.get_or_create(
        material="Hierro Forjado", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Aluminio", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Acero", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Madera", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Celotex", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Celotex Asfaltado", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Concreto", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Teca", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Forja", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(
        material="Resina", tipo_material=cat)

    cat = TipoMaterial.objects.get_or_create(
        tipo_de_material="(Ejemplo) Hilos")[0]
    OpcionMaterial.objects.get_or_create(material="ACE", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="ACR", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="ALG", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="ASD01", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="ASDPE", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="COS", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="HUL", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="OLE", tipo_material=cat)

    cat = TipoMaterial.objects.get_or_create(
        tipo_de_material="(Ejemplo) Cordones")[0]
    OpcionMaterial.objects.get_or_create(material="BAM", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="CHE", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="BOU", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="CIN", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="FET", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="GIM", tipo_material=cat)

    cat = TipoMaterial.objects.get_or_create(
        tipo_de_material="(Ejemplo) Otros")[0]
    OpcionMaterial.objects.get_or_create(material="CRO", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="TUL", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="LEN", tipo_material=cat)
    OpcionMaterial.objects.get_or_create(material="PER", tipo_material=cat)

    cat = CategoriaProducto.objects.get_or_create(
        categoria="(Ejemplo) Bancas")[0]
    CategoriaProducto.objects.get_or_create(
        categoria="(Ejemplo) Metalicas", categoria_padre=cat)
    CategoriaProducto.objects.get_or_create(
        categoria="(Ejemplo) Madera", categoria_padre=cat)

    CategoriaProducto.objects.get_or_create(categoria="(Ejemplo) Pasamaneria")
