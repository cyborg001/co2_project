# import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Usuario(models.Model):
    cantidad_habitantes = models.IntegerField()
    estrato_se = models.CharField(max_length=50) #estrato socioeconomico
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
   
    def __str__(self):
        return f'Usuario {self.pk}, dep: {self.departamento}, mun: {self.municipio}'

class Pregunta(models.Model):
    # el tag puede ser: gas natural, energia electrica, glp
    tag = models.CharField(max_length=75)

    seleccion = models.IntegerField()
    unidad = models.CharField(max_length=20)
    respuesta_consumo = models.FloatField()
    fecha_pub = models.DateTimeField('fecha publicada')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seleccion} para {self.tag} es {self.respuesta_consumo}'