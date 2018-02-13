# coding:utf8   
# Christian Manalo Mañibo
# 13/02/2018

dividendo=input("Escriba el dividendo: ")
divisor=input("Escriba el divisor: ")


if divisor == 0:
    print "No se puede dividir entre 0."
else:
    if dividendo % divisor  == 0:
        print "La división es exacta. Cociente: " ,  dividendo / divisor
    else:
        print "La división no es exacta. Cociente: " , dividendo / divisor, "Resto: ", dividendo % divisor 

