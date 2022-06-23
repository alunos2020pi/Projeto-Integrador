from django.test import TestCase
from ofertas.models import Supermercado, Loja
from django.contrib.auth.models import User

class SupermercadoTestCase(TestCase):
    def setUp(self):
        
        author = User.objects.create(
        username='testing',
        password='password@@#',
        first_name='test name',
        email='test@test.test',
        )  

        Supermercado.objects.create(nome="Supermercado Teste", informante = author)

    def test_supermercado_create(self):
        supermercado = Supermercado.objects.get(nome="Supermercado Teste")
        self.assertEqual(supermercado.nome, "Supermercado Teste")

    def test_supermercado_instance(self):
        supermercado = Supermercado.objects.get(name="Supermercado Teste")
        self.assertEquals(isinstance(supermercado), Supermercado)
        