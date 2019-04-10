from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = PhoneNumberField()
    email = models.EmailField()
    funcao = models.CharField(max_length=50)
    gestor = models.CharField(max_length=50)
    #contratacao = models.DateField()


class Aso(models.Model):
    data_primeiro = models.DateField()
    data_proximo = models.DateField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)







