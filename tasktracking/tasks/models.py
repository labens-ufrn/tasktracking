from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

class Tag(models.Model):
    nome = models.CharField(max_length=50)

class Link(models.Model):
    nome = models.CharField(max_length=50)
    url = models.URLField()
    def __str__(self):
        self.nome
        self.url


class Tarefa(models.Model):
    STATUS_CHOICES = (
        ("1", "Planejada"),
        ("2", "Em Execução"),
        ("3", "Concluída"),
        ("4", "Cancelada"),
    )
    SITUACAO_CHOICES = (
        ("1", "Aberta"),
        ("2", "Abandonada"),
        ("3", "Fechada"),
    )

    identificador = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    descrição = models.CharField(max_length=250)
    criada_em = models.DateTimeField(auto_now_add=True)
    fechada_em = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES)

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Execucao(models.Model):
    """[summary]

    Args:
        models ([type]): [Representa uma execução de uma tarefa.]
    """
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    tarefa = models.ForeignKey(Tarefa, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
