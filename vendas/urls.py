from django.urls import path
from .views import FazerVenda, ConfirmarVenda, ListaVendas

app_name = 'vendas'

urlpatterns = [
    path('nova/', FazerVenda.as_view(), name='venda_create'),
    path('confirmar/', ConfirmarVenda.as_view(), name='venda_confirm'),
    path('historico/', ListaVendas.as_view(), name='venda_list'),
]
