# Generated by Django 3.0.2 on 2021-11-13 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0004_supermercado_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('lograd', models.CharField(max_length=50)),
                ('num', models.PositiveIntegerField()),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2)),
                ('cep', models.CharField(help_text='Formato 00000-000', max_length=9)),
                ('sm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ofertas.Supermercado')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
