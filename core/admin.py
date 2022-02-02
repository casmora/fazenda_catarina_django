from django.contrib import admin

from core.models import Categoria, Compra, ItensCompra, Produto, Produtor, Regiao

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Produtor)
admin.site.register(Regiao)


class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)  
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)  