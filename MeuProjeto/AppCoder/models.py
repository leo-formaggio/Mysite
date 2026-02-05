from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.IntegerField()

    def __str__(self):
        return self.nome

class Entrega(models.Model):
    nome = models.CharField(max_length=100)
    data_entrega = models.DateField()
    entregue = models.BooleanField()

    def __str__(self):
        return self.nome
    

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username