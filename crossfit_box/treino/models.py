from django.db import models

class Training(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao_minutos = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
