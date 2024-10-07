from django.db import models
from django.contrib.auth.models import User
import re

class Alimento(models.Model):
    nome = models.CharField(max_length=500)
    carboidratos_totais_100g = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    carboidratos_disponiveis_100g = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    carboidratos_totais_200ml = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    carboidratos_disponiveis_200ml = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    link = models.URLField(max_length=500)

    def save(self, *args, **kwargs):
        self.nome = re.sub(r'<<.*?>>', '', self.nome).strip()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'alimentos'

    def __str__(self):
        return self.nome


class Refeicao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    horario = models.DateTimeField()
    

    def __str__(self):
        return f"{self.usuario} - (Horario: {self.horario.strftime('%Y-%m-%d %H:%M:%S')})"