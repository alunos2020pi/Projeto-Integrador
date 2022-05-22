from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ofertas.views import index, about, ofertasporsuper, ondeencontrar, ProdutoListView, SupermercadoListView, Em_OfertaListView, SupermercadoCreate, LojaCreate, ProdutoCreate, Em_OfertaCreate



class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_ofertaporsuper_url_is_resolved(self):
        url = reverse('ofertasporsuper', args=[1])
        self.assertEquals(resolve(url).func, ofertasporsuper)
    
    def test_ondeencontrar_url_is_resolved(self):
        url = reverse('ondeencontrar', args=[1])
        self.assertEquals(resolve(url).func, ondeencontrar)

    ## Class Based Views Testing

    def test_ProdutoListView_url_is_resolved(self):
        url = reverse('produtos')
        self.assertEquals(resolve(url).func.view_class, ProdutoListView)

    def test_SupermercadoListView_url_is_resolved(self):
        url = reverse('supermercados')
        self.assertEquals(resolve(url).func.view_class, SupermercadoListView)

    def test_Em_OfertaListView_url_is_resolved(self):
        url = reverse('ofertas')
        self.assertEquals(resolve(url).func.view_class, Em_OfertaListView)

    def test_SupermercadoCreate_url_is_resolved(self):
        url = reverse('supermercado-create')
        self.assertEquals(resolve(url).func.view_class, SupermercadoCreate)
    
    def test_LojaCreate_url_is_resolved(self):
        url = reverse('loja-create')
        self.assertEquals(resolve(url).func.view_class, LojaCreate)
    
    def test_ProdutoCreate_url_is_resolved(self):
        url = reverse('produto-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProdutoCreate)
    
    def test_Em_Oferta_url_is_resolved(self):
        url = reverse('em_oferta-create')
        self.assertEquals(resolve(url).func.view_class, Em_OfertaCreate)