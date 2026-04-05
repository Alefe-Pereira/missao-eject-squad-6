from django.db import models

class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data = models.DateField()
    hora = models.TimeField()
    numero_pessoas = models.PositiveIntegerField()
    observacoes = models.TextField(blank=True)
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
    trecho = models.TextField(max_length=300)
    conteudo = models.TextField()
    data_publicacao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

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