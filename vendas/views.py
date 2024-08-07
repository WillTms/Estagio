from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Sum
from django.db.models.functions import TruncDate
from .models import Cliente, Produto, Venda, ItensVenda
from django.views.generic.list import ListView

class VendaListView(View):
    def get(self, request):
        vendas_por_dia = (
            Venda.objects
            .annotate(data=TruncDate('data_venda'))
            .values('data')
            .annotate(total_dia=Sum('total'))
            .order_by('-data')
        )

        vendas_detalhadas = (
            Venda.objects
            .annotate(data=TruncDate('data_venda'))
            .order_by('-data_venda')
        )

        context = {
            'vendas_por_dia': vendas_por_dia,
            'vendas_detalhadas': vendas_detalhadas,
        }
        return render(request, 'vendas/vendas_list.html', context)

class VendaCreateView(View):
    def get(self, request):
        clientes = Cliente.objects.all()
        produtos = Produto.objects.filter(estado=True)
        return render(request, 'vendas/vendas_form.html', {
            'clientes': clientes,
            'produtos': produtos,
        })

    def post(self, request):
        cliente_id = request.POST.get('cliente')
        cliente = get_object_or_404(Cliente, id=cliente_id)
        produtos = Produto.objects.filter(estado=True)
        itens_venda = []

        total = 0.0
        for produto in produtos:
            quantidade = int(request.POST.get(f'quantidade_{produto.id}', 0))
            if quantidade > 0:
                preco = produto.preco_venda  # Sempre usar o preco_venda
                subtotal = quantidade * preco
                item = {
                    'produto': produto,
                    'quantidade': quantidade,
                    'preco': preco,
                    'subtotal': subtotal
                }
                itens_venda.append(item)
                total += subtotal

        # Passa os detalhes da venda para o template de pré-visualização
        return render(request, 'vendas/venda_preview.html', {
            'cliente': cliente,
            'itens_venda': itens_venda,
            'total': total
        })

class VendaConfirmView(View):
    def post(self, request):
        cliente_id = request.POST.get('cliente_id')
        cliente = get_object_or_404(Cliente, id=cliente_id)
        venda = Venda(cliente=cliente)
        venda.save()
        
        produtos = Produto.objects.filter(estado=True)
        total = 0.0

        for produto in produtos:
            quantidade = int(request.POST.get(f'quantidade_{produto.id}', 0))
            if quantidade > 0:
                preco = produto.preco_venda  # Sempre usar o preco_venda
                item_venda = ItensVenda(
                    venda=venda,
                    produto=produto,
                    quantidade=quantidade,
                    preco=preco
                )
                item_venda.save()
                total += item_venda.get_subtotal()
        
        venda.total = total
        venda.save()

        return redirect('vendas:venda_create')
