from django.db import models
from django.urls import reverse

# Create your models here.

class Supermercado(models.Model):
    nome = models.CharField(max_length=50, help_text='Insira o nome de um mercado')
    imagem = models.ImageField(upload_to='supermercados/%Y/%m/%d', blank=True)
    site = models.CharField(max_length=50, help_text='Insira o site com http://', blank=True)
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('ofertasporsuper', args=[str(self.id)])
        
class Loja(models.Model):
    sm = models.ForeignKey('Supermercado', on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=50)
    lograd = models.CharField(max_length=50)
    num = models.PositiveIntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    
    ESTADOS = (
        ('AC',	'Acre'),
        ('AL',	'Alagoas'),
        ('AP',	'Amapá'),
        ('AM',	'Amazonas'),
        ('BA',	'Bahia'),
        ('CE',	'Ceará'),
        ('DF',	'Distrito Federal'),
        ('ES',	'Espírito Santo'),
        ('GO',	'Goiás'),
        ('MA',	'Maranhão'),
        ('MT',	'Mato Grosso'),
        ('MS',	'Mato Grosso do Sul'),
        ('MG',	'Minas Gerais'),
        ('PA',	'Pará'),
        ('PB',	'Paraíba'),
        ('PR',	'Paraná'),
        ('PE',	'Pernambuco'),
        ('PI',	'Piauí'),
        ('RJ',	'Rio de Janeiro'),
        ('RN',	'Rio Grande do Norte'),
        ('RS',	'Rio Grande do Sul'),
        ('RO',	'Rondônia'),
        ('RR',	'Roraima'),
        ('SC',	'Santa Catarina'),
        ('SP',	'São Paulo'),
        ('SE',	'Sergipe'),
        ('TO',	'Tocantins'),
    )
    
    estado = models.CharField(
        max_length=2,
        choices=ESTADOS,
        default='SP',
    )
    
    cep = models.CharField(max_length=9, help_text='Formato 00000-000')
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome}: {self.lograd}, {self.num} - {self.bairro} - {self.cidade}-{self.estado} CEP:{self.cep}'
    
    def get_absolute_url(self):
        return reverse('ofertasporsuper', args=[str(self.sm.id)])
        
class Produto(models.Model):
    desc = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    qtd = models.FloatField()
    
    UNIDADES = (
        ('cx','caixa'),
        ('g','grama'),
        ('gl','galão'),
        ('kg','quilo'),
        ('l','litro'),
        ('ml','mililitro'),
        ('pc','pacote'),
        ('pç','peça'),
        ('unid','unidade')
    )    
    
    unid = models.CharField(
        max_length=10,
        choices=UNIDADES
    )
    
    obs = models.CharField(max_length=50, null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/%Y/%m/%d', blank=True)
    
    class Meta:
        ordering = ['desc', 'marca','qtd']
        
    def __str__(self):
        if self.obs:
            return f'{self.desc} {self.marca}, {self.qtd} {self.unid}, {self.obs}'
        else:
            return f'{self.desc} {self.marca}, {self.qtd} {self.unid}'
        
    def get_absolute_url(self):
	    return reverse('ondeencontrar', args=[str(self.id)])

        
class Em_Oferta(models.Model):
    sm = models.ForeignKey('Supermercado', on_delete=models.SET_NULL, null=True)
    pd = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    inicio = models.DateField(null=True, blank=True)
    fim = models.DateField(null=True, blank=True)
    obs = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['pd','preco']
        verbose_name = 'Em oferta'
        verbose_name_plural = 'Em oferta'

    
    def __str__(self):
        return f'Produto {self.pd} em oferta no mercado {self.sm} de {self.inicio} a {self.fim}'
		
    def get_absolute_url(self):
        return reverse('ofertas')