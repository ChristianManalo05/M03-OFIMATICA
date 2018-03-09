# coding: utf8
# Christian Mañibo
# 09/03/2018


import os
os.system("clear")

print"""

-----BUCLE CONTAR-----

"""

# Inicializaciones
salir = "N"
num=1
limit=input("Hasta cuanto quieres contar?: ")

if (num<limit) :
    while ( salir=="N" ):
        # Hago cosas
        print num
    
        # Incremento
        num = num + 1
        # Activo indicador de salida si toca
        if ( num>limit ): # Condición de salida
            salir = "S"
else :
    while ( salir=="N" ):
        # Hago cosas
        print num
    
        # Incremento
        num = num - 1
        # Activo indicador de salida si toca
        if ( num<limit ): # Condición de salida
            salir = "S"
