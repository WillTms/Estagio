from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

from utils.validacpf import valida_cpf

class Cliente(models.Model):
    nome_cliente = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Nome Cliente')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    telefone = models.CharField(max_length=11)
    divida = models.FloatField(verbose_name= 'Valor da Dívida')
    #data_venda = models.DateField(verbose_name= 'Tempo da Dívida', default=) teste nulo
    endereco = models.CharField(max_length=50, verbose_name='Endereço')
    numero = models.CharField(max_length=5, verbose_name='Número')
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.usuario}'

    def clean(self):
        mensagem_erro = {}

        if not valida_cpf(self.cpf):
            mensagem_erro['cpf'] = 'Digite um CPF válido'
            
        if mensagem_erro:
            raise ValidationError(mensagem_erro)

    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    