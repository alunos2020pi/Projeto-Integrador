# Generated by Django 3.0.2 on 2022-06-17 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ofertas', '0008_em_oferta_fonte'),
    ]

    operations = [
        migrations.AddField(
            model_name='em_oferta',
            name='informante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loja',
            name='informante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='informante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supermercado',
            name='informante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='em_oferta',
            name='fonte',
            field=models.CharField(choices=[('Panfleto', 'Panfleto'), ('Funcionário', 'Funcionário'), ('Cliente', 'Cliente'), ('Site', 'Site')], default='Panfleto', max_length=15),
        ),
    ]