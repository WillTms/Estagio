from django.contrib import admin
from . import models

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco_compra','preco_venda', 'quantidade']

admin.site.register(models.Produto, ProdutoAdmin)


