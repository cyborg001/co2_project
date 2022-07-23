from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('hola mundo')

def calculo_co2(tag, seleccion, usuario):
    preguntas = usuario.pregunta_set.all()
    FEE = 0.18 # Factor de emision de energia electrica en kgCO2/kWh
    VPKWH = 518.94 # Valor promedio del kWh electrico
    ICIE = 3 # Indicador de columna indirecto electrio
    ICVPE = 17 # Indicador de columna indirecto del valor promedio electrico 
    FEEE_SIN = 0.18 # Factor de emision de energia electrica del SIN en kgCO2/kWh
    FECOC = 1.98 # Factor de emision de gas natural generico en kgCO2/m3
    CFPGN = 3406.309259 # Cargo fijo promedio de gas propano en $COP
    CVPGN = 1672.633704 # Costo variable promedio de gas propano en $/m3

    consumo_electrico1 = ''
    consumo_electrico2 = ''
    consumo_electrico3 = ''


    
    if preguntas[0].tag == 'ENERGIA ELECTRICA':
        if preguntas[0].seleccion == 2:
            consumo_electrico2 = preguntas[0].consumo
        if preguntas[0].seleccion == 1:
            consumo_electrico1 = preguntas[0].consumo # en kWh/mes
        if preguntas[0].seleccion == 3:
            consumo_electrico3 == preguntas[0].consumo
    total_kwh_mes2 =  consumo_electrico2 / VPKWH 
    emisiones2 = (total_kwh_mes2*ICIE) * FEEE_SIN/no_residentes/1000

    pass


























          
