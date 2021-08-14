from django.db import models

# Create your models here.


class produto(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    fornecedor = models.CharField(max_length=100)
    quantidade = models.IntegerField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome