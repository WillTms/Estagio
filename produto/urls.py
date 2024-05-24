from django.urls import path 
#from . import views
from produto.views import AdicionarProduto,Lista,EditarProduto,ExcluirProduto

app_name = 'produto'

urlpatterns = [
    path('adicionarproduto/',AdicionarProduto.as_view(), name="adicionarproduto"),
    path('',Lista.as_view(), name="listaproduto"),
    path("editarproduto/<int:pk>", EditarProduto.as_view(), name="editarproduto"),
    path('excluirproduto/<int:pk>', ExcluirProduto.as_view(), name='excluirproduto'),

    #path('lista/', views.ListaProdutos.as_view(), name="lista"),
    #path('<slug>', views.DetalheProdutos.as_view(), name="detalhe"),
    #path('adicionaravenda/', views.AdicionarAVEnda.as_view(), name="adicionaravenda"),
    #path('removerdavenda/', views.RemoverDaVenda.as_view(), name="removerdavenda"),
    #path('carrinhovenda/', views.CarrinhoVenda.as_view(), name="carrinhovenda"),
    #path('finalizar/', views.Finalizar.as_view(), name="finalizar")
]

