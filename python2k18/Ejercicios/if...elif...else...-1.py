# coding:utf8   
# Christian Manalo Mañibo
# 12/02/2018

dividiendo=input("Escriba el dividiendo: ")

divisor=input("Escriba el divisor: ")

cociente= dividiendo // divisor
resto= dividiendo % divisor 


if dividiendo % divisor == 0:
    print "La división es exacta. Cociente: " ,  cociente
else:
    print "La división no es exacta. Cociente: " , cociente, "Resto: ", resto 
