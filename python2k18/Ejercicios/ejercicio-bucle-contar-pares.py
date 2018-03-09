# coding: utf8
# Christian Mañibo
# 09/03/2018


import os
os.system("clear")

print"""

-----BUCLE CONTAR PARES-----

"""

# Inicializaciones
salir = "N"
num=0
limit=input("Hasta cuanto quieres contar? (Números Pares): ")

if (num<limit) :
    while ( salir=="N" ):
        # Hago cosas
        if num%2==0:
            print num
    
        # Incremento
        num = num + 2
        # Activo indicador de salida si toca
        if ( num>limit ): # Condición de salida
            salir = "S"
else :
    while ( salir=="N" ):
        # Hago cosas
        if num%2==0:
            print num
    
        # Incremento
        num = num - 2
        # Activo indicador de salida si toca
        if ( num<limit ): # Condición de salida
            salir = "S"
