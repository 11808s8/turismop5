# from django.db import models
from django.contrib.gis.db import models
from improved_user.model_mixins import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomUser(AbstractUser):
    is_guia = models.BooleanField('guia status', default=False)
    is_cliente = models.BooleanField('cliente status', default=False)
    pass
    # email = models.EmailField(unique=True)

    # USERNAME_FIELD='email'
    # def __str__(self):
    #     return self.email

# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Pessoa.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.pessoa.save()

class Pessoa(models.Model):
    usuario = models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=0, primary_key=True)
    nome = models.CharField(max_length=100)
    
    telefone = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Pessoa_Fisica(Pessoa):
    # pessoa = models.OneToOneField(Pessoa,on_delete=models.CASCADE
    # )
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=14)

class Pessoa_Juridica(Pessoa):
    # pessoa = models.OneToOneField(Pessoa,on_delete=models.CASCADE,
    # )
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
    guias = models.ManyToManyField(Pessoa_Juridica)


class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    rota = models.ForeignKey(Atrativo, on_delete = models.CASCADE)
    guias = models.ForeignKey(Pessoa_Juridica, on_delete=None)
    avaliacao = models.FloatField()


