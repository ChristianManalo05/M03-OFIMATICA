# coding: utf8
# Christian Mañibo
# 21/03/2018

# Inicializaciones
numero=int(input("Introduce un número: "))
valor=1
contador=0
salir="N"

while (salir=="N") :
    # Hago cosas
    if(numero%2==0): 
        contador=contador+1
        
    # Activo indicador de salida si toca
    if(numero==valor): # Condición de salida
        salir="S"

    valor=valor+1

if (contador>2):
    print (numero , "no es un numero primo")

else:
    print (numero , "es un numero primo")
