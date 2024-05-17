from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import UpdateView, CreateView, DeleteView
from django.views import View
from django.http import HttpResponse
#from . import models
from .models import Produto
from django.urls import reverse_lazy
'''class AdicionarProduto(View):
      def get(self, *args, **kwargs):
        return HttpResponse('adicionar produto')
'''
'''def AdicionarProduto(request):
    form = ProdutosForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'novo_produto.html', {'form': form})
'''

class AdicionarProduto(CreateView):
  model = Produto
  fields = ['nome', 'quantidade', 'preco_compra', 'preco_venda', 'preco_promocional', 'descricao','slug']
  success_url = reverse_lazy('produto:lista cliente')

class EditarProduto(UpdateView):
  model = Produto
  fields = ['nome', 'quantidade', 'preco_compra', 'preco_venda', 'preco_promocional', 'descricao','slug']
  success_url = reverse_lazy('produto:lista cliente')  
  
   
class Lista(ListView):
  model = Produto






"""class ListaProdutos(ListView):
      model = models.Produto
      template_name = 'produto/lista.html'
      context_object_name = 'produtos'    
   """ 
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
