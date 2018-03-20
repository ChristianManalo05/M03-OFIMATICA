
# coding: utf8
# Christian Mañibo
# 11/03/2018

import os
os.system("clear")

print"###### BUCLE SUMAR 1 ######"

# Inicializaciones
salir = "N"
num = 1
resultado = 0
while ( salir=="N" ):
    # Hago cosas
    print "        " ,	num

    # Incremento
    resultado = resultado + num
    num = num + 1
    
    # Activo indicador de salida si toca
    if ( num > 5): # Condición de salida
        salir = "S"
        print "       ",resultado


