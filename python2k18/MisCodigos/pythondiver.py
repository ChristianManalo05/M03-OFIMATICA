# coding: utf-8
# Christian Mañibo
# 05/02/18

print "EXAMEN FINAL DE LA UNIVERSIDAD"


#Pregunta el nombre
nombre=raw_input ("Introduce tu nombre:")

#Te da la bienvenida con tu nombre
print "Bienvenido" , nombre

#Pregunta si has estudiado
estudiar=raw_input("Has estudiado S/N?:")

if estudiar== "S" :
	print "Hoy aprovarás,", nombre ,"El Fvcking Master" 
	
else:
#Pregunta si has jugado
	jugar=raw_input("Has jugado S/N?:")
	if jugar== "S" :
		print "Espabila" , nombre
	
	else:
		print "Lo conseguirás por los pelos, suerte" , nombre
