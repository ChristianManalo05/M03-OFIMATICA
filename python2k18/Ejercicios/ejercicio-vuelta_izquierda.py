#coding: utf8
# Christian Manalo Mañibo
# 15/03/2018


import os
os.system ("clear")

# Variables
salir="N"
giro=input("Donde desea girar, derecha o izquierda? D/I: ")
vuelta=1

while ( salir=="N" ):

# Hago cosas
        #Si es derecha
    if giro.upper()=="D":
        if vuelta%8==1 or vuelta%8==2 :
                print (vuelta ,"-> arriba")
        elif vuelta%8==3 or vuelta%8==4 :
                print (vuelta , "-> derecha")
        elif vuelta%8==5 or vuelta%8==6 :
                print (vuelta , "-> abajo")
        elif vuelta%8==7 or vuelta%8==0 :
                print (vuelta ,"-> izquierda")

        #Si es izquierda
    if giro.upper()=="I":
        if vuelta%8==1 or vuelta%8==2 :
            print (vuelta ,"-> arriba")
        elif vuelta%8==7 or vuelta%8==0 :
            print (vuelta , "-> derecha")
        elif vuelta%8==5 or vuelta%8==6 :
            print (vuelta , "-> abajo")
        elif vuelta%8==3 or vuelta%8==4 :
            print (vuelta ,"-> izquierda")

    # Incremento
    vuelta = vuelta + 1 

    # Activo indicador de salida si toca
    if (vuelta >8): # Condición de salida

        salir = "S"
print ("FIN DE LAS VUELTAS")
