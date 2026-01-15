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