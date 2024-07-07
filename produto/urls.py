from django.urls import path 
#from . import views
from produto.views import AdicionarProduto,Lista,EditarProduto,ExcluirProduto

app_name = 'produto'

urlpatterns = [
    path('adicionarproduto/',AdicionarProduto.as_view(), name="adicionarproduto"),
    path('',Lista.as_view(), name="listaproduto"),
    path("editarproduto/<int:pk>", EditarProduto.as_view(), name="editarproduto"),
    path('excluirproduto/<int:pk>', ExcluirProduto.as_view(), name='excluirproduto'),

]

