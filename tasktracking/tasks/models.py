from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    """
        Gabriel Gonçalo
    Args:
        models ([type]): [description]
    """
    nome = models.CharField(max_length=200)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nome


class Tag(models.Model):
    """
        Jonas
    Args:
        models ([type]): [description]
    """
    nome = models.CharField(max_length=50)
    tarefa = models.ForeignKey('Tarefa', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome


class Link(models.Model):
    """
        Wanessa
    Args:
        models ([type]): [description]
    """
    nome = models.CharField(max_length=50)
    url = models.URLField()
    tarefa = models.ForeignKey('Tarefa', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome + ' ' + self.url


class Tarefa(models.Model):
    """
        Arthur
    Args:
        models ([type]): [description]
    """
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
    fechada_em = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.identificador + ' - ' + self.nome


class Execucao(models.Model):
    """[summary]
        Pedro
    Args:
        models ([type]): [Representa uma execução de uma tarefa.]
    """
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    tarefa = models.ForeignKey(Tarefa, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
