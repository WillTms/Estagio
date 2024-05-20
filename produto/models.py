#from django.conf import settings
#import os
#from PIL import Image
from django.db import models
from django.utils.text import slugify
#from utils import utils


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=1)
    preco_compra = models.FloatField(verbose_name='Preço Compra:')
    preco_venda = models.FloatField(verbose_name='Preço Venda:')
    preco_promocional = models.FloatField(blank=True, null=True, verbose_name='Preço Promoção:')
    descricao = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descrição:')
    slug = models.SlugField(unique=True, blank=True, null=True)
    


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
