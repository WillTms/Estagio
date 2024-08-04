from django.contrib import admin
from . import models

class ListaItens(admin.TabularInline):
    model = models.ItensVenda
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    inlines = [
        ListaItens
    ]

admin.site.register(models.Venda, VendaAdmin)
admin.site.register(models.ItensVenda)

