from django.db import models
from django.utils.text import slugify



class Produto(models.Model):
    nome = models.CharField(max_length=255,verbose_name='Nome Produto:')
    quantidade = models.PositiveIntegerField(default=0,verbose_name='Quantidade:')
    preco_compra = models.FloatField(verbose_name='Preço Compra:')
    preco_venda = models.FloatField(verbose_name='Preço Venda:')
    descricao = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descrição:')
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome

    def get_preco_final(self):
        """
        Retorna o preço final do produto, considerando a promoção se disponível.
        """
        return self.preco_promocional if self.preco_promocional else self.preco_venda
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    
