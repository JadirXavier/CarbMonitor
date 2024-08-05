from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Refeicao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    horario = models.DateTimeField()

    def carboidratos_totais(self):
        total = sum([item.carboidratos_totais() for item in self.refeicaoalimento_set.all()])
        return total

    def __str__(self):
        return f"{self.usuario} - (Horario: {self.horario.strftime('%Y-%m-%d %H:%M:%S')})"