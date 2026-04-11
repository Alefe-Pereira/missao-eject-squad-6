from django.test import TestCase, Client
from django.urls import reverse
from .models import Reserva, ArtigoBlog, Destaque
import datetime

class ReservaModelTest(TestCase):

    def test_criar_reserva(self):
        reserva = Reserva.objects.create(
            nome="João Silva",
            data=datetime.date(2026, 5, 10),
            hora=datetime.time(19, 0),
            numero_pessoas=2
        )
        self.assertEqual(reserva.nome, "João Silva")
        self.assertEqual(reserva.numero_pessoas, 2)

    def test_str_reserva(self):
        reserva = Reserva.objects.create(
            nome="Maria Santos",
            data=datetime.date(2026, 5, 15),
            hora=datetime.time(20, 0),
            numero_pessoas=4
        )
        self.assertIn("Maria Santos", str(reserva))

    def test_ordenacao_reservas(self):
        Reserva.objects.create(
            nome="Cliente A",
            data=datetime.date(2026, 5, 10),
            hora=datetime.time(18, 0),
            numero_pessoas=2
        )
        Reserva.objects.create(
            nome="Cliente B",
            data=datetime.date(2026, 5, 20),
            hora=datetime.time(19, 0),
            numero_pessoas=3
        )
        reservas = Reserva.objects.all()
        self.assertEqual(reservas[0].nome, "Cliente B")


class ArtigoBlogModelTest(TestCase):

    def test_criar_artigo(self):
        artigo = ArtigoBlog.objects.create(
            titulo="Teste de Artigo",
            trecho="Trecho do artigo de teste",
            data_publicacao=datetime.date(2026, 3, 10)
        )
        self.assertEqual(artigo.titulo, "Teste de Artigo")

    def test_str_artigo(self):
        artigo = ArtigoBlog.objects.create(
            titulo="Artigo Teste",
            trecho="Trecho",
            data_publicacao=datetime.date(2026, 3, 10)
        )
        self.assertEqual(str(artigo), "Artigo Teste")

    def test_ordenacao_artigos(self):
        ArtigoBlog.objects.create(
            titulo="Artigo Antigo",
            trecho="Trecho",
            data_publicacao=datetime.date(2026, 1, 1)
        )
        ArtigoBlog.objects.create(
            titulo="Artigo Recente",
            trecho="Trecho",
            data_publicacao=datetime.date(2026, 6, 1)
        )
        artigos = ArtigoBlog.objects.all()
        self.assertEqual(artigos[0].titulo, "Artigo Recente")


class DestaqueModelTest(TestCase):

    def test_criar_destaque(self):
        destaque = Destaque.objects.create(
            titulo="Chef's capacitados",
            descricao="Nossa equipe especializada.",
            ordem=1
        )
        self.assertEqual(destaque.titulo, "Chef's capacitados")
        self.assertEqual(destaque.ordem, 1)

    def test_str_destaque(self):
        destaque = Destaque.objects.create(
            titulo="Premiações",
            descricao="Reconhecido por revistas.",
            ordem=3
        )
        self.assertEqual(str(destaque), "Premiações")


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.artigo = ArtigoBlog.objects.create(
            titulo="Artigo para teste de view",
            trecho="Trecho do artigo",
            data_publicacao=datetime.date(2026, 3, 10)
        )

    def test_home_status_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_blog_status_200(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_artigo_status_200(self):
        response = self.client.get(reverse('artigo', args=[self.artigo.id]))
        self.assertEqual(response.status_code, 200)

    def test_sobre_status_200(self):
        response = self.client.get(reverse('sobre'))
        self.assertEqual(response.status_code, 200)

    def test_criar_reserva_post(self):
        response = self.client.post(reverse('criar_reserva'), {
            'nome': 'Pedro Teste',
            'data': '2026-05-10',
            'hora': '19:00',
            'numero_pessoas': '2'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reserva.objects.count(), 1)
        self.assertEqual(Reserva.objects.first().nome, 'Pedro Teste')