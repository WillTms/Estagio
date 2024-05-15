from django.db import models
from django.contrib.auth.models import User

class Venda(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    valor_total = models.FloatField()
    qtd_total = models.IntegerField()
    
    def __str__(self):
        return f'Venda N. {self.pk}'


class ItemDaVenda(models.Model):
    pedido = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.IntegerField()
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0, blank=True, null=True)
    quantidade = models.IntegerField()
   
    def __str__(self):
        return f'Produto do {self.Venda}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'