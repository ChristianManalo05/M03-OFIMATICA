# coding: utf8
# Christian Manalo Mañibo
# 09/03/2018

# Inicializaciones

import os
os.system("clear")

print """
########################################################################

		                BUCLE CONTAR

########################################################################"""


salir = "N"
num=input("A partir de cuanto quieres empezar contar?: ")
limit=input("Hasta cuando quieres contar?: ")

while ( salir=="N" ):
    # Hago cosas
    print num

    # Incremento
    num = num + 1
    # Activo indicador de salida si toca
    if ( num>limit ): # Condición de salida
            salir = "S"
