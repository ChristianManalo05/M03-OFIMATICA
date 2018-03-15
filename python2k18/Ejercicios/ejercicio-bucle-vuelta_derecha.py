#coding: utf8
# Christian Manalo Mañibo
# 15/03/2018


import os
os.system ("clear")

# Variables
salir ="N"
vuelta=1

while ( salir=="N" ):
	
	# Hago cosas
	if suma%8==1 or suma%8==2 :
		print (vuelta ,"-> arriba")
	elif suma%8==3 or suma%8==4 :
		print (vuelta , "-> derecha")
	elif suma%8==5 or suma%8==6 :
		print (vuelta , "-> abajo")
	elif suma%8==7 or suma%8==0 :
		print (vuelta ,"-> izquierda")

	# Incremento
	vuelta = vuelta + 1 

	# Activo indicador de salida si toca
	if (vuelta >8): # Condición de salida
		
		salir = "S"
print ("FIN DE LAS VUELTAS")
