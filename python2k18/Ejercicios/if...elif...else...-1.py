# coding:utf8   
# Christian Manalo Mañibo
# 12/02/2018

dividendo=input("Escriba el dividiendo: ")

divisor=input("Escriba el divisor: ")

cociente= dividendo / divisor
resto= dividendo % divisor 


if resto == 0:
    print "La división es exacta. Cociente: " ,  cociente
else:
    print "La división no es exacta. Cociente: " , cociente, "Resto: ", resto 
