# Generated by Django 5.0.4 on 2024-05-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug:'),
        ),
    ]
