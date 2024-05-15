from django.urls import path 
from . import views


app_name = 'vendas'

urlpatterns = [
    path('pagar/<int:pk>', views.Pagar.as_view(), name='pagar'),
    path('salvarvenda/', views.SalvarVenda.as_view(), name='salvarvenda'),
    path('lista/', views.Lista.as_view(), name='lista'),
    path('detalhe/<int:pk>', views.Detalhe.as_view(), name='detalhe'),
]
