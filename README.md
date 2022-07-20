# co2_project
contiene una app (co2_app) que mide la contaminacion de co2 generada por una familia 

# Entendiendo el modelo Pregunta
- El modelo pregunta posee un atributo tag que indica el tipo de recurso que se consume
  puede ser ENERGIA ELECTRICA, GAS NATURAL O GLP
 - El atributo seleccion es un entero entre 1 y 3
  1 si el consumo es el promedio mensual de la vivienda de <energia electrica o gas> en <kwh/mes>
  2 si el costo promedio mensual del valor de la factura de <energia electrica o gas> en <unidad>
  3 si es el consumo promedio de la vivienda de <energia o gas> por estrato social en <unidad>
 - El atributo unidad representa la unidad de medida del bien consumido
 - El atributo respuesta_consumo es un numero de coma flotante que cuantifica lo consumido
 - El atributo fecha_pub es la fecha cuando se creo esa pregunta/usuario
 - El atributo usuario es el usuario que dueno de la vivienda
 
 # Entendiendo el modelo Usuario
 - El atributo id es un numero unico en orden de creacion asignado al usuario
 - El atributo cantidad_de_habitates es el numero de familiares en la vivienda
 - El atributo estrato_se es el estrato socio economico del usuario
 - El atributo departamento es el barrio donde vive el usuario
 - El atributo municipio es el municipio/provincia donde vive el usuario
  
  
  

