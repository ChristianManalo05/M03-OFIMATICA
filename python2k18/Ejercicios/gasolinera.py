# coding: utf8
# Christian Manalo Mañibo
# 22/02/2018


import os

os.system("clear")

print """
########################################################################
#**********************************************************************#
#                                                                      #
#                      BIENVENIDO A LA GASOLINERA                      #
#                                                                      #
#**********************************************************************#
########################################################################
"""

tabla=raw_input("Quiere ver la tabla de gasolina? si/no: ")

if tabla.lower ()=="si":
    print """

########################################################################
#                                                                      #
#                       _______________________                        #
#                       |                     |                        #
#                       | -TABLA DE GASOLINA- |                        #
#                       |_____________________|                        #
#                                                                      #
#   1-| Super Normal               --------------->   = 1,5  $/l       #
#                                                                      #
#   2-| Super Turbo                --------------->   = 1,55 $/l       #
#                                                                      #
#   3-| Sin Plomo Normal           --------------->   = 1,6  $/l       #
#                                                                      #
#   4-| Sin Plomo Sabor Naranja    --------------->   = 1,65 $/l       #
#                                                                      #
#   5-| Diesel Normal              --------------->   = 1,7  $/l       #
#                                                                      #
#   6-| Diesel Fast & Furius       --------------->   = 1,75 $/l       #
#                                                                      #
########################################################################
"""
    tipo_gasolina=input("Que tipo de gasolina quiere? Elija un numero: ")
    if tipo_gasolina<=0 or tipo_gasolina>7:
        print "Este producto no existe. Que tenga un buen dia."
        
    elif tipo_gasolina==1:
        print "Ha elegido Super Normal."
        litros=input("Quantos litros desea?: ")
        if litros<=0:
            print "Este valor no es valido. Que tenga un buen dia."
        else:
            print "Ha introducido" , litros , "litros, en total són" , litros*1.50,"€"
    
    elif tipo_gasolina==2:
        print "Ha elegido Super Turbo."
        litros=input("Quantos litros desea?: ")
        if litros<=0:
            print "Este valor no es valido. Que tenga un buen dia."
        else:
            print "Ha introducido" , litros , "litros, en total són" , litros*1.55,"€"
   
    elif tipo_gasolina==3:
        print "Ha elegido Sin Plomo Normal."
        litros=input("Quantos litros desea?: ")
        if litros<=0:
            print "Este valor no es valido. Que tenga un buen dia."
        else:
            print "Ha introducido" , litros , "litros, en total són" , litros*1.60,"€"
   
    elif tipo_gasolina==4:
        print "Ha elegido Sin Plomo Sabor Naranja."
        litros=input("Quantos litros desea?: ")
        if litros<=0:
            print "Este valor no es valido. Que tenga un buen dia."
        else:
            print "Ha introducido" , litros , "litros, en total són" , litros*1.65,"€"
   
    elif tipo_gasolina==5:
        print "Ha elegido Diesel Normal."
        litros=input("Quantos litros desea?: ")
        if litros<=0:
            print "Este valor no es valido. Que tenga un buen dia."
        else:
            print "Ha introducido" , litros , "litros, en total són" , litros*1.70,"€"
   
    elif tipo_gasolina==6:
        print "Ha elegido Diesel Fast & Furius."
        litros=input("Quantos litros desea?: ")
        if litros<=0:
            print "Este valor no es valido. Que tenga un buen dia."
        else:
            print "Ha introducido" , litros , "litros, en total són" , litros*1.75,"€"                
elif tabla.lower ()=="no":
    print """
########################################################################
#**********************************************************************#
#                                                                      #
#                         BYE BYE , CUIDATE!!!                         #
#                                                                      #
#**********************************************************************#
########################################################################
"""

else: 
    print """
########################################################################
#**********************************************************************#
#                                                                      #
#                    ERROR ERROR , ADIOS CUIDATE!!!                    #
#                                                                      #
#**********************************************************************#
########################################################################
"""
