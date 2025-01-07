from django.db import models


class Member(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=24, blank=False, null=False)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome