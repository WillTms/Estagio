# Generated by Django 5.0.4 on 2024-08-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='E-mail'),
        ),
    ]