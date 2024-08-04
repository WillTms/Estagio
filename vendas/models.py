from django.db import models
from clientes.models import Cliente
from produto.models import Produto

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vendas')
    data_venda = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return f'Venda {self.id} - Cliente: {self.cliente.nome_cliente} - Total: {self.total}'

    def calcular_total(self):
        total = sum(item.get_subtotal() for item in self.itens.all())
        self.total = total
        self.save()
        return total

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

class ItensVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.FloatField(default=0.0)

    def get_subtotal(self):
        return self.quantidade * self.preco

    def save(self, *args, **kwargs):
        # Atualiza o estoque do produto ao salvar o item de venda
        produto = self.produto
        produto.quantidade -= self.quantidade
        if produto.quantidade < 0:
            raise ValueError('Quantidade de produto em estoque insuficiente.')
        produto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'

    class Meta:
        verbose_name = 'Item de Venda'
        verbose_name_plural = 'Itens de Venda'
