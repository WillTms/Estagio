# Generated by Django 5.0.4 on 2024-08-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_remove_cliente_bairro_remove_cliente_complemento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(default='teste@gmail.com', max_length=40, null=True, verbose_name='E-mail'),
        ),
    ]