from django.urls import path
from .views import FazerVenda, ConfirmarVenda, ListaVendas, GerarVendaPDF, GerarRelatorioMensalPDF
from . import views

app_name = 'vendas'

urlpatterns = [
    path('nova/', FazerVenda.as_view(), name='venda_create'),
    path('confirmar/', ConfirmarVenda.as_view(), name='venda_confirm'),
    path('historico/', ListaVendas.as_view(), name='venda_list'),
    path('vendas/<int:venda_id>/pdf/', GerarVendaPDF.as_view(), name='venda_pdf'),
     path('relatorio-mensal-pdf/', GerarRelatorioMensalPDF.as_view(), name='relatorio_mensal_pdf'),
]
