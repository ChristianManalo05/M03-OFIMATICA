# coding: utf8
# Christian Mañibo
# 13/03/2018


import os
os.system("clear")

print "###### BUCLE SUMAR 2 ######"

# Inicializaciones
salir = "N"
num = 1
maximo=5
resultado = 0


while ( salir=="N" ):
    # Hago cosas
    
    if (num%2==0): # Es par

       print num
        
       resultado = resultado + num
            
    # Incremento
    
    num = num + 1
    
    # Activo indicador de salida si toca
    if ( num > maximo): # Condición de salida
        salir = "S"

print "=", resultado
