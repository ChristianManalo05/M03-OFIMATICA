# coding: utf8
# Christian Mañibo
# 09/03/2018

# Inicializaciones
salir = "N"
num = 1
resultado = num 
while ( salir=="N" ):
    # Hago cosas
    print num

    # Incremento
    num = num + 1
    resultado = num + resultado
    # Activo indicador de salida si toca
    if ( num > resultado ): # Condición de salida
        salir = "S"
        print """
             RESULTADO
        --------------------
        """   , resultado
