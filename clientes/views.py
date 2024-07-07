from django.views import View
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import UpdateView, CreateView
from django.views import View
from .models import Cliente
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db import models
from django.db.models import Q

#--------Adicionar produto

class AdicionarCliente(CreateView):
    model = Cliente
    fields = ['nome_cliente', 'cpf', 'telefone', 'email']
    success_url = reverse_lazy('clientes:listacliente')


#--------Lista de produtos

class ListaClientes(ListView):
  model = Cliente
  template_name = 'clientes/cliente_list.html'
  context_object_name = 'cliente_list'
  
  def get_queryset(self):
        query = self.request.GET.get('busca')
        if query:
            return Cliente.objects.filter(Q(nome__icontains=query), estado=True).order_by('id')
        return Cliente.objects.filter(estado=True).order_by('id')

#-------Excluir os produtos

class ExcluirCliente(View):
    def post(self, request, *args, **kwargs):
        cliente_id = kwargs.get('pk')
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            cliente.estado = False  
            cliente.save()
            return JsonResponse({'success': True})
        except Cliente.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Cliente não encontrado'})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'success': False, 'error': 'Método GET não permitido para exclusão de cliente'})

#--------------Editar os produtos

class EditarCliente(UpdateView):
  model = Cliente
  fields = ['nome_cliente', 'cpf', 'telefone', 'email']
  success_url = reverse_lazy('clientes:listacliente') 
  
  

