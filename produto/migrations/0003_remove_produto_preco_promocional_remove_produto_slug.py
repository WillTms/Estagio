# Generated by Django 5.0.4 on 2024-10-26 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produto_estado_alter_produto_quantidade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='preco_promocional',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='slug',
        ),
    ]
