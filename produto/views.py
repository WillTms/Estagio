from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

'''class AdicionarProduto(View):
      def get(self, *args, **kwargs):
        return HttpResponse('adicionar produto')
'''  
class ListaProdutos(ListView):
      model = models.Produto
      template_name = 'produto/lista.html'
      context_object_name = 'produtos'    
    
class DetalheProdutos(View):
      def get(self, *args, **kwargs):
        return HttpResponse('detalhe produto')

class AdicionarAVEnda(View):
      def get(self, *args, **kwargs):
        return HttpResponse('adicionar a venda')

class RemoverDaVenda(View):
      def get(self, *args, **kwargs):
        return HttpResponse('remover da venda')

class CarrinhoVenda(View):
      def get(self, *args, **kwargs):
        return HttpResponse('carrinho venda')

class Finalizar(View):
      def get(self, *args, **kwargs):
        return HttpResponse('finalizar')
