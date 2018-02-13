# coding:utf8   
# Christian Manalo Mañibo
# 13/02/2018

dividendo=input("Escriba el dividiendo: ")
divisor=input("Escriba el divisor: ")

cociente= dividiendo // divisor
resto= dividiendo % divisor 

if divisor == 0:
    print "No se puede dividir entre 0."
else:
    if dividiendo % divisor == 0:
        print "La división es exacta. Cociente: " ,  cociente
    else:
        print "La división no es exacta. Cociente: " , cociente, "Resto: ", resto 
