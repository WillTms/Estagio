from django.urls import path 
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProdutos.as_view(), name="detalhe"),
    #path('adicionarproduto/', views.AdicionarProduto.as_view(), name="adicionarproduto"),
    path('adicionaravenda/', views.AdicionarAVEnda.as_view(), name="adicionaravenda"),
    path('removerdavenda/', views.RemoverDaVenda.as_view(), name="removerdavenda"),
    path('carrinhovenda/', views.CarrinhoVenda.as_view(), name="carrinhovenda"),
    path('finalizar/', views.Finalizar.as_view(), name="finalizar")
]

