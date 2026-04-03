from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField(unique=True)
    faltas = models.IntegerField("default=0")

class aulas(models.Model):
    aula = models.CharField(max_length=100, default="0", unique=True)
    