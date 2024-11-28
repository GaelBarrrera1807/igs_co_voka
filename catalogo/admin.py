from django.contrib import admin

from .models import OpcionColor
from .models import OpcionMaterial
from .models import TipoColor
from .models import TipoMaterial
from .models import TipoParte


@admin.register(TipoParte)
class TipoParteAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_de_parte')


@admin.register(TipoColor)
class TipoColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_de_color')


@admin.register(OpcionColor)
class OpcionColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'tipo_color')
    list_filter = ('tipo_color',)


@admin.register(TipoMaterial)
class TipoMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_de_material')


@admin.register(OpcionMaterial)
class OpcionMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'tipo_material')
    list_filter = ('tipo_material',)
