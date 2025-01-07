from django.db import models
from mebros.models import Member
from treino.models import Training

class WorkoutPlan(models.Model):
    membro = models.ForeignKey(Member, related_name='planos', on_delete=models.CASCADE)
    treino = models.ForeignKey(Training, related_name='planos', on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __str__(self):
        return f'{self.membro.nome} - {self.treino.nome}'
