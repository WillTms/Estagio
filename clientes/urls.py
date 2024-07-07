from django.urls import path 
from . import views
from clientes.views import AdicionarCliente,ListaClientes,EditarCliente,ExcluirCliente

app_name = 'clientes'

urlpatterns = [
    path('adicionarcliente/',AdicionarCliente.as_view(), name="adicionarcliente"),
    path('listacliente/',ListaClientes.as_view(), name="listacliente"),
    path("editarcliente/<int:pk>", EditarCliente.as_view(), name="editarcliente"),
    path('excluircliente/<int:pk>', ExcluirCliente.as_view(), name='excluircliente'),
]