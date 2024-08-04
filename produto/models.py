from django.db import models
from django.utils.text import slugify



class Produto(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField(default=0)
    preco_compra = models.FloatField(verbose_name='Preço Compra:')
    preco_venda = models.FloatField(verbose_name='Preço Venda:')
    preco_promocional = models.FloatField(blank=True, null=True, verbose_name='Preço Promoção:')
    descricao = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descrição:')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Slug:')
    estado = models.BooleanField(default=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

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
        
    
