# coding: utf8
# Christian Mañibo
# 13/03/2018
# Corrección/Mejora

import os
os.system("clear")

print "###### BUCLE SUMAR ######"

# Inicializaciones
salir = "N"
num = 1
maximo=5
resultado = 0


while ( salir=="N" ):
    # Hago cosas
    print num,
    if (num<= maximo-1):
        print "+" ,
    # Incremento
    resultado = resultado + num
    num = num + 1
    
    # Activo indicador de salida si toca
    if ( num > 5): # Condición de salida
        salir = "S"

print "=", resultado


"""
# coding: utf8
# Christian Mañibo
# 11/03/2018

import os
os.system("clear")

print"###### BUCLE SUMAR ######"

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

"""
