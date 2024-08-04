from django.urls import path
from .views import VendaCreateView, VendaConfirmView, VendaListView

app_name = 'vendas'

urlpatterns = [
    path('nova/', VendaCreateView.as_view(), name='venda_create'),
    path('confirmar/', VendaConfirmView.as_view(), name='venda_confirm'),
    path('historico/', VendaListView.as_view(), name='venda_list'),
]
