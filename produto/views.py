from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import UpdateView, CreateView, DeleteView
from django.views import View
from django.http import HttpResponse
from .models import Produto
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db import models
from django.db.models import Q



class Lista(ListView):
  model = Produto
  template_name = 'produto_list.html'
  context_object_name = 'produto_list'

  def get_queryset(self):
        query = self.request.GET.get('busca')
        if query:
            return Produto.objects.filter(Q(nome__icontains=query)).order_by('id')
        return Produto.objects.all().order_by('id')


class AdicionarProduto(CreateView):
  model = Produto
  fields = ['nome', 'quantidade', 'preco_compra', 'preco_venda', 'preco_promocional', 'descricao','slug']
  success_url = reverse_lazy('produto:listaproduto')
  

  def form_valid(self, form):
        return super().form_valid(form)

class EditarProduto(UpdateView):
  model = Produto
  fields = ['nome', 'quantidade', 'preco_compra', 'preco_venda', 'preco_promocional', 'descricao','slug']
  success_url = reverse_lazy('produto:listaproduto')  
  
class ExcluirProduto(DeleteView):
  model = Produto
  success_url = reverse_lazy('produto:listaproduto')

  def post(self, request, *args, **kwargs):
      self.object = self.get_object()
      self.object.delete()
      return JsonResponse({'success': True})
    
  def get(self, request, *args, **kwargs):
      return redirect(self.success_url) 






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
