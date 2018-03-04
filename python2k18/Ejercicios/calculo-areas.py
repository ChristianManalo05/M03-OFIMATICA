#coding: utf8
#Christian Mañibo
#4/3/2018

import os
os.system("clear")

from math import pi

print """
####################################################

                CALCULADORA DE AREAS

####################################################
"""

print """

T) Triángulo
C) Circulo 

"""

figura=raw_input("Que figura quieres calcular (T/C)? ")

if figura.upper() == "T" :
	
    base=input ("Introduzca la Base: ")
    altura=input ("Introduzca la Altura: ")
    
    if(base<0) or (altura<0) :
        print "No existe las medidas negativas" 
    else :
        area=(base*altura)/2
        print "L'area es igual a ", area
elif figura.upper() == "C":
    radi=input ("Introdueix el radi: ")
    
    if (radi<0) :
        print "No existe las medidas de negativas"
    else :
        print "L'area es igual a ", round (pi*radi**2,2)
else :
    print "Elija una figura valida, T o C"
