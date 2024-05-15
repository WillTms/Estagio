from django.shortcuts import render
#rom django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('criar cliente')

class Editar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('editar cliente')

class Excluir(View):
    def get(self, *args, **kwargs):
        return HttpResponse('excluir cliente')


