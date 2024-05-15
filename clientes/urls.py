from django.urls import path 
from . import views

app_name = 'clientes'

urlpatterns = [
    path('criar/', views.Criar.as_view(), name='criar'),
    path('editar/', views.Editar.as_view(), name='editar'),
    path('excluir/', views.Excluir.as_view(), name='excluir'),
]