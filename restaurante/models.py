from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    numero_pessoas = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.data} as {self.hora}"

    class Meta:
        ordering = ['-data', '-hora']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'


class ArtigoBlog(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='blog/')
    legenda = models.TextField(max_length=300, blank=True, null=True)
    trecho = models.TextField(max_length=300)
    primeiro_paragrafo = models.TextField(max_length=400, null=True)
    segundo_paragrafo = models.TextField(max_length=400, null=True)
    terceiro_paragrafo = models.TextField(max_length=400, null=True)
    quarto_paragrafo = models.TextField(max_length=400, null=True)
    data_publicacao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=50, null=True)
    autor_imagem = models.ImageField(upload_to='autores', null=True)
    citacao1 = models.TextField(null=True)
    citacao2 = models.TextField(null=True)
    segunda_imagem = models.ImageField(upload_to='sub_imagem', null=True)
    legenda2 = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = 'Artigo do Blog'
        verbose_name_plural = 'Artigos do Blog'


class Destaque(models.Model):
    icone = models.ImageField(upload_to='destaques/')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Destaque'
        verbose_name_plural = 'Destaques'


class Funcionario(models.Model): #Classe dos funcionários para edição do blog
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario.username
    
