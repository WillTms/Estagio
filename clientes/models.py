from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

from utils.validacpf import valida_cpf

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=30, verbose_name='Nome do Cliente')
    cpf = models.CharField(max_length=11, verbose_name='CPF', null=True, blank=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    email = models.CharField(max_length=40, verbose_name='E-mail', null=True, blank=True)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.nome_cliente}'

    def clean(self):
        mensagem_erro = {}

        if not valida_cpf(self.cpf):
            mensagem_erro['cpf'] = 'Digite um CPF válido'
            
        if mensagem_erro:
            raise ValidationError(mensagem_erro)

    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    