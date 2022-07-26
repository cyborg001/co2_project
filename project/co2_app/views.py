from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Pregunta
# Create your views here.
def index(request):
    u = Usuario.objects.all()[0]
    # print(u.pregunta_set.get(tag='E')
    emision = calculo_co2('Energia Electrica',u)
    return HttpResponse(F'hola mundo {emision}')

def calculo_co2(tag, usuario):
    pregunta = usuario.pregunta_set.get(tag=tag)
    print(pregunta.seleccion)
    print(pregunta)
    FEE = 0.18 # Factor de emision de energia electrica en kgCO2/kWh
    VPKWH = 518.94 # Valor promedio del kWh electrico
    ICIE = 3 # Indicador de columna indirecto electrio
    ICVPE = 17 # Indicador de columna indirecto del valor promedio electrico 
    FEEE_SIN = 0.18 # Factor de emision de energia electrica del SIN en kgCO2/kWh
    FECOC = 1.98 # Factor de emision de gas natural generico en kgCO2/m3
    CFPGN = 3406.309259 # Cargo fijo promedio de gas propano en $COP
    CVPGN = 1672.633704 # Costo variable promedio de gas propano en $/m3

    departamento = usuario.departamento
    municipio = usuario.municipio
    total_kwh_mes2 =  consumo / VPKWH 
    emisiones2 = (total_kwh_mes2*ICIE) * FEEE_SIN/no_residentes/1000
    estrato_social = usuario.estrato_se
    no_residentes = usuario.cantidad_habitantes
    consumo = pregunta.respuesta_consumo
    seleccion = pregunta.seleccion
    emisiones = ''
    print(pregunta)
    # if tag == 'ENERGIA ELECTRICA':
    #     if seleccion == 2:
    #         print(pregunta)
    #         total_kwh_mes2 =  consumo / VPKWH 
    #         emisiones = (total_kwh_mes2*ICIE) * FEEE_SIN/no_residentes/1000
    #     if seleccion == 1:
    #         consumo_electrico1 = consumo # en kWh/mes
    #     if seleccion == 3:
    #         consumo == consumo
    # elif tag == 'GAS NATURAL':
    #     if seleccion == 2:
    #         consumo_gas_propano2 = consumo
    #     if seleccion == 1:
    #         consumo_gas_propano1 = consumo # en kWh/mes
    #     if seleccion == 3:
    #         consumo == consumo
    # else:
    #     if seleccion == 2:
    #         consumo_glp2 = consumo
    #     if seleccion == 1:
    #         consumo_glp1 = consumo # en kWh/mes
    #     if seleccion == 3:
    #         consumo == consumo

    

    return emisiones


























          
