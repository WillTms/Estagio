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
from django.db import IntegrityError


#--------Adicionar produto
class AdicionarProduto(CreateView):
    model = Produto
    fields = ['nome', 'quantidade', 'preco_compra', 'preco_venda', 'preco_promocional', 'descricao','slug']
    success_url = reverse_lazy('produto:listaproduto')

    def form_valid(self, form):
        try:
            if form.cleaned_data['quantidade'] < 0:
                form.add_error('quantidade', 'O valor não pode ser negativo.')
                return self.form_invalid(form)
        
            if form.cleaned_data['preco_compra'] < 0:
                form.add_error('preco_compra', 'O valor não pode ser negativo.')
                return self.form_invalid(form)
        
            if form.cleaned_data['preco_venda'] < 0:
                form.add_error('preco_venda', 'O valor não pode ser negativo.')
                return self.form_invalid(form)
        
            if Produto.objects.filter(slug=form.cleaned_data['slug']).exists():
                mensagem_erro = "Já existe um produto com este slug. Por favor, escolha outro."
                form.add_error('slug', mensagem_erro)
                return self.form_invalid(form)
            
            return super().form_valid(form)
        except IntegrityError:
            mensagem_erro = "Ocorreu um erro ao adicionar o produto."
            form.add_error(None, mensagem_erro)
            return self.form_invalid(form)

#--------Lista de produtos
class Lista(ListView):
  model = Produto
  template_name = 'produto_list.html'
  context_object_name = 'produto_list'

  def get_queryset(self):
        query = self.request.GET.get('busca')
        if query:
            return Produto.objects.filter(Q(nome__icontains=query), estado=True).order_by('id')
        return Produto.objects.filter(estado=True).order_by('id')

#-------Excluir os produtos
class ExcluirProduto(View):
    success_url = reverse_lazy('produto:listaproduto')

    def post(self, request, *args, **kwargs):
        produto_id = kwargs.get('pk')
        produto = Produto.objects.get(id=produto_id)
        produto.estado= False
        produto.save()
        return JsonResponse({'success': True})
    
    def get(self, request, *args, **kwargs):
        return redirect(self.success_url) 


#--------------Editar os produtos
class EditarProduto(UpdateView):
  model = Produto
  fields = ['nome', 'quantidade', 'preco_compra', 'preco_venda', 'preco_promocional', 'descricao','slug']
  success_url = reverse_lazy('produto:listaproduto') 
  
  def form_valid(self, form):
        if form.cleaned_data['quantidade'] < 0:
            form.add_error('quantidade', 'O valor não pode ser negativo.')
            return self.form_invalid(form)
        
        if form.cleaned_data['preco_compra'] < 0:
            form.add_error('preco_compra', 'O valor não pode ser negativo.')
            return self.form_invalid(form)
        
        if form.cleaned_data['preco_venda'] < 0:
            form.add_error('preco_venda', 'O valor não pode ser negativo.')
            return self.form_invalid(form)
        
        if form.cleaned_data.get('preco_promocional') is not None and form.cleaned_data['preco_promocional'] < 0:
            form.add_error('preco_promocional', 'O valor não pode ser negativo.')
            return self.form_invalid(form)
        
        return super().form_valid(form) 
  
  
  
  

