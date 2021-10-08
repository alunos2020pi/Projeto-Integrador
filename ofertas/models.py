from django.db import models

# Create your models here.

class Supermercado(models.Model):
    nome = models.CharField(max_length=50, help_text='Insira o nome de um mercado')
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
        
class Produto(models.Model):
    desc = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    qtd = models.PositiveIntegerField()
    unid = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['desc', 'marca','qtd']
        
    def __str__(self):
        return f'{self.desc} {self.marca}, {self.qtd} {self.unid}, {self.obs}'

        
class Em_Oferta(models.Model):
    sm = models.ForeignKey('Supermercado', on_delete=models.SET_NULL, null=True)
    pd = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    inicio = models.DateField(null=True, blank=True)
    fim = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['pd','preco']
        verbose_name = 'Em oferta'
        verbose_name_plural = 'Em oferta'

    
    def __str__(self):
        return f'Produto {self.pd} em oferta no mercado {self.sm} de {self.inicio} a {self.fim}'