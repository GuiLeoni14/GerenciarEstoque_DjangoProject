from django.db import models

# Create your models here.


class produto(models.Model):
    STATUS = (
        ('', 'Selecione:'),
        ('Cosmético', 'Cosmético'),
        ('Industrial', 'Industrial'),
        ('Alimentício', 'Alimentício'),
    )
    ESTADOS = (
        ('Disponível', 'Disponível'),
        ('Vendido', 'Vendido'),
    )
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=100,
        choices=STATUS,
        )
    descricao = models.CharField(max_length=100)#textfild
    data = models.DateField()
    fornecedor = models.CharField(max_length=100)
    quantidade = models.IntegerField(max_length=100)
    estado = models.CharField(
        max_length=12,
        choices=ESTADOS,
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome