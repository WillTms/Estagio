from django.shortcuts import render
#from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('pagar')

class SalvarVenda(View):
    def get(self, *args, **kwargs):
        return HttpResponse('salvar venda')

class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalhe')

class Lista(View):
    def get(self, *args, **kwargs):
        return HttpResponse('lista')