#coding: utf8
# Christian Manalo Mañibo
# 15/03/2018


import os
os.system ("clear")

print "-EJERCICIO BUCLE : VUELTA DERECHA-"
# Variables
salir="N"
vuelta=1

while ( salir=="N" ):
	
	# Hago cosas
	if vuelta%8==1 or vuelta%8==2 :
		print vuelta ,"-> arriba"
	elif vuelta%8==3 or vuelta%8==4 :
		print vuelta , "-> derecha"
	elif vuelta%8==5 or vuelta%8==6 :
		print vuelta , "-> abajo"
	elif vuelta%8==7 or vuelta%8==0 :
		print vuelta ,"-> izquierda"

	# Incremento
	vuelta = vuelta + 1 

	# Activo indicador de salida si toca
	if (vuelta >8): # Condición de salida
		
		salir = "S"
print "FIN DE LAS VUELTAS"
