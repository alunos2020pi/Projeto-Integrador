# Generated by Django 3.0.2 on 2021-11-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0003_auto_20211011_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='supermercado',
            name='site',
            field=models.CharField(blank=True, help_text='Insira o site com http://', max_length=50),
        ),
    ]