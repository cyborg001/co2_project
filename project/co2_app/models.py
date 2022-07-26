# import datetime
from django.db import models

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

# class Constante(models.model):

#     FEE = 0.18 # Factor de emision de energia electrica en kgCO2/kWh
#     VPKWH = 518.94 # Valor promedio del kWh electrico
#     ICIE = 3 # Indicador de columna indirecto electrio
#     ICVPE = 17 # Indicador de columna indirecto del valor promedio electrico 
#     FEEE_SIN = 0.18 # Factor de emision de energia electrica del SIN en kgCO2/kWh
#     FECOC = 1.98 # Factor de emision de gas natural generico en kgCO2/m3
#     CFPGN = 3406.309259 # Cargo fijo promedio de gas propano en $COP
#     CVPGN = 1672.633704 # Costo variable promedio de gas propano en $/m3