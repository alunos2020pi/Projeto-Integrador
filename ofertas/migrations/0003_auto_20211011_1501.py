# Generated by Django 3.0.2 on 2021-10-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0002_auto_20211008_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='produtos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='supermercado',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='supermercados/%Y/%m/%d'),
        ),
    ]
