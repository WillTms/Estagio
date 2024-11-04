from django.urls import path
from .views import (
    FazerVenda, ConfirmarVenda, ListaVendas, GerarVendaPDF, GerarRelatorioMensalPDF, 
    ListaVendasPendentes, MarcarVendaComoPaga, PesquisaProdutoView
)

app_name = 'vendas'

urlpatterns = [
    path('nova/', FazerVenda.as_view(), name='venda_create'),
    path('confirmar/', ConfirmarVenda.as_view(), name='venda_confirm'),
    path('historico/', ListaVendas.as_view(), name='venda_list'),
    path('vendas/<int:venda_id>/pdf/', GerarVendaPDF.as_view(), name='venda_pdf'),
    path('relatorio-mensal-pdf/', GerarRelatorioMensalPDF.as_view(), name='relatorio_mensal_pdf'),
    path('vendas/pendentes/', ListaVendasPendentes.as_view(), name='lista_pendentes'),
    path('vendas/marcar-paga/<int:venda_id>/', MarcarVendaComoPaga.as_view(), name='marcar_paga'),
    path('pesquisa_produto/', PesquisaProdutoView.as_view(), name='pesquisa_produto'),
]
