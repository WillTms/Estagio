# Generated by Django 5.0.4 on 2024-07-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_alter_itensvenda_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itensvenda',
            name='preco_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='itensvenda',
            name='quantidade',
            field=models.PositiveIntegerField(),
        ),
    ]
