# Generated by Django 5.0.4 on 2024-05-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_rename_descricao_curta_produto_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_promocional',
            field=models.FloatField(blank=True, null=True, verbose_name='Preço Promoção:'),
        ),
    ]
