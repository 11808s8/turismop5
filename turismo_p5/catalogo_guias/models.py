# from django.db import models
from django.contrib.gis.db import models
from improved_user.model_mixins import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass
    # email = models.EmailField(unique=True)

    # USERNAME_FIELD='email'
    # def __str__(self):
    #     return self.email

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    
    telefone = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Pessoa_Fisica(Pessoa):
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=14)

class Pessoa_Juridica(Pessoa):
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=150)
    avaliacao = models.FloatField()
    numeroRegistro = models.PositiveIntegerField()

class Chat(models.Model):
    mensagens = models.TextField()

class Protocolo(models.Model):
    id_conta = models.IntegerField()
    descricao = models.TextField()
    quantia = models.FloatField()
    data = models.DateField()


class Ponto(models.Model):
    geom = models.PointField()


# não sei se ficará assim msm
class Mapa(models.Model):
    pontos = models.ForeignKey(Ponto, on_delete=None)


class Atrativo(models.Model):
    nome = models.CharField(max_length=100)
    infos = models.TextField()
    ponto = models.ForeignKey(Ponto, on_delete=models.CASCADE)


class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    rota = models.ForeignKey(Atrativo, on_delete = models.CASCADE)
    guias = models.ForeignKey(Pessoa_Juridica, on_delete=None)
    avaliacao = models.FloatField()


