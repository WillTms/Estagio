from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Sum
from django.db.models.functions import TruncDate
from .models import Cliente, Produto, Venda, ItensVenda
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.utils.timezone import now
from calendar import monthrange
from datetime import datetime
from django.contrib import messages  
from django.db.models import Q



class PesquisaProdutoView(View):
    def get(self, request):
        query = request.GET.get('busca')
        produtos = Produto.objects.filter(estado=True)
        if query:
            produtos = produtos.filter(Q(nome__icontains=query))
        
        return render(request, 'vendas/pesquisa_produtos.html', {
            'produtos': produtos,
        })


#-------------Pagar Pendencias
class MarcarVendaComoPaga(View):
    def post(self, request, venda_id):
        venda = get_object_or_404(Venda, id=venda_id)
        venda.status = 'paga'
        venda.save()
        return redirect('vendas:lista_pendentes')

#-------------Vendas Pendentes
class ListaVendasPendentes(View):
    def get(self, request):
        vendas_pendentes = Venda.objects.filter(status='pendente').order_by('data_venda')
        return render(request, 'vendas/vendas_pendentes.html', {
            'vendas_pendentes': vendas_pendentes,
        })

 #-----------------Gerar relatorio
class GerarRelatorioMensalPDF(View):
    def get(self, request):
        mes_ano = request.GET.get('mes')  
        if mes_ano:
            ano, mes = map(int, mes_ano.split('-'))  
            primeiro_dia = datetime(ano, mes, 1)
            ultimo_dia = datetime(ano, mes, monthrange(ano, mes)[1])
            
            vendas = Venda.objects.filter(data_venda__date__gte=primeiro_dia, data_venda__date__lte=ultimo_dia, status='paga')

            total_mes = vendas.aggregate(Sum('total'))['total__sum'] or 0  

            context = {
                'total_mes': total_mes,
                'ano': ano,
                'mes': mes,
                'vendas': vendas,
            }

            template_path = 'vendas/relatorio_mensal.html'
            html = render_to_string(template_path, context)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="relatorio_vendas_{ano}_{mes}.pdf"'

            pisa_status = pisa.CreatePDF(html, dest=response)

            if pisa_status.err:
                return HttpResponse(status=400)
            return response
        else:
            return HttpResponse(status=400)

#-------------------Gerar PDF
class GerarVendaPDF(View):
    def get(self, request, venda_id):
        venda = get_object_or_404(Venda.objects.filter(status='paga'), id=venda_id)
        itens_venda = venda.itens.all()

        context = {
            'venda': venda,
            'itens_venda': itens_venda
        }

        template_path = 'vendas/relatorio_venda.html'
        html = render_to_string(template_path, context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="relatorio_venda_{venda.id}.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Erro ao gerar PDF', status=400)
        return response

#-------------------------- Lista de Vendas
class ListaVendas(View):
    def get(self, request):
        vendas_por_dia = (
            Venda.objects
            .filter(status='paga')
            .annotate(data=TruncDate('data_venda'))
            .values('data')
            .annotate(total_dia=Sum('total'))
            .order_by('-data')
        )

        vendas_detalhadas = (
            Venda.objects
            .filter(status='paga')
            .annotate(data=TruncDate('data_venda'))
            .order_by('-data_venda')
        )

        hoje = now()
        ano = hoje.year
        atual_mes = hoje.month

        context = {
            'vendas_por_dia': vendas_por_dia,
            'vendas_detalhadas': vendas_detalhadas,
            'ano': ano,
            'atual_mes': atual_mes,
        }
        return render(request, 'vendas/vendas_list.html', context)

#------------------- Fazer Vendas

class FazerVenda(View):
    def get(self, request):
        clientes = Cliente.objects.filter(estado=True)
        
        termo_pesquisa = request.GET.get('busca')
        if termo_pesquisa:
            produtos = Produto.objects.filter(estado=True, nome__icontains=termo_pesquisa)
        else:
            produtos = Produto.objects.filter(estado=True)
        
        return render(request, 'vendas/vendas_form.html', {
            'clientes': clientes,
            'produtos': produtos,
            'termo_pesquisa': termo_pesquisa  
        })

    def post(self, request):
        cliente_id = request.POST.get('cliente')
        cliente = None
        if cliente_id:
            cliente = get_object_or_404(Cliente, id=cliente_id)
        
        produtos = Produto.objects.filter(estado=True)
        itens_venda = []

        total = 0.0
        for produto in produtos:
            quantidade = int(request.POST.get(f'quantidade_{produto.id}', 0))
            if quantidade > 0:
                preco = produto.preco_venda  
                subtotal = quantidade * preco
                item = {
                    'produto': produto,
                    'quantidade': quantidade,
                    'preco': preco,
                    'subtotal': subtotal
                }
                itens_venda.append(item)
                total += subtotal

        return render(request, 'vendas/venda_preview.html', {
            'cliente': cliente,
            'itens_venda': itens_venda,
            'total': total
        })

#-------------------Tela de Confirmar Vendas
class ConfirmarVenda(View):
    def post(self, request):
        cliente_id = request.POST.get('cliente_id')
        cliente = None
        if cliente_id:
            cliente = get_object_or_404(Cliente, id=cliente_id)

        status_venda = request.POST.get('status') 

        if not cliente and status_venda == 'pendente':
            messages.error(request, "Apenas clientes registrados podem deixar a venda pendente.")
            return redirect('vendas:venda_preview')  

        valor_final = request.POST.get('valor_final')
        if valor_final:
            valor_final = float(valor_final)
        else:
            valor_final = None  

        venda = Venda(cliente=cliente)
        venda.save()
        
        produtos = Produto.objects.filter(estado=True)
        total = 0.0

        for produto in produtos:
            quantidade = int(request.POST.get(f'quantidade_{produto.id}', 0))
            if quantidade > 0:
                preco = produto.preco_venda
                item_venda = ItensVenda(
                    venda=venda,
                    produto=produto,
                    quantidade=quantidade,
                    preco=preco
                )
                item_venda.save()
                total += item_venda.get_subtotal()

        venda.total = valor_final if valor_final else total
        venda.status = status_venda
        venda.save()

        if status_venda == 'paga':
            return redirect('vendas:venda_list')  
        else:
            return redirect('vendas:lista_pendentes')  

