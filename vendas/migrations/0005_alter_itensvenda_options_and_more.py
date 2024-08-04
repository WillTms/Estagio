# Generated by Django 5.0.4 on 2024-08-03 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_remove_cliente_bairro_remove_cliente_complemento_and_more'),
        ('vendas', '0004_itensvenda_preco_total_alter_itensvenda_quantidade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itensvenda',
            options={'verbose_name': 'Item de Venda', 'verbose_name_plural': 'Itens de Venda'},
        ),
        migrations.RemoveField(
            model_name='itensvenda',
            name='preco_total',
        ),
        migrations.RemoveField(
            model_name='itensvenda',
            name='preco_venda',
        ),
        migrations.AddField(
            model_name='itensvenda',
            name='preco',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='itensvenda',
            name='quantidade',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='itensvenda',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='vendas.venda'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas', to='clientes.cliente'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]