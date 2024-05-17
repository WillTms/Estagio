from django.urls import path 
#from . import views
from produto.views import AdicionarProduto,Lista,EditarProduto

app_name = 'produto'

urlpatterns = [
    #path('adicionarproduto/', views.AdicionarProduto, name='adicionarproduto'),
    #path('sucesso/', views.sucesso, name='sucesso'),  
    #path('lista/', views.ListaProdutos.as_view(), name="lista"),
    #path('<slug>', views.DetalheProdutos.as_view(), name="detalhe"),
    
    path('adicionarproduto/',AdicionarProduto.as_view(), name="adicionarproduto"),
    path('',Lista.as_view(), name="lista cliente"),
    path("editarproduto/<int:pk>", EditarProduto.as_view(), name="editarproduto"),
    #path('adicionaravenda/', views.AdicionarAVEnda.as_view(), name="adicionaravenda"),
    #path('removerdavenda/', views.RemoverDaVenda.as_view(), name="removerdavenda"),
   # path('carrinhovenda/', views.CarrinhoVenda.as_view(), name="carrinhovenda"),
    #path('finalizar/', views.Finalizar.as_view(), name="finalizar")
]

