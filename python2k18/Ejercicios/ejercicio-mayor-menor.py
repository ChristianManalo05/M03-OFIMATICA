# coding:utf8
# Christian Manalo Mañibo
# 11/02/2018

A=input("Introduce valor A: ")
B=input("Introduce valor B: ")
C=input("Introduce valor C: ")

if (A==B) and (A==C) :
    print "Hay 3 valores iguales"
else:
    if  ((A==B) and (A!=C)) or ((B==C) and (B!=A)) or ((A==C) and (C!=B)):
        print "Hay 2 valores iguales"
    else:
        if (A>B) and (A>C) :
            if B<C :
                print "Valor A es mayor y Valor B es menor"
            else:
                print "Valor A es mayor y Valor C es menor"
        else:
            if (B>A) and (B>C) :
                if A<C :
                    print "Valor B es mayor y Valor A es menor"
                else:
                    print "Valor B es mayor y Valor C es menor"
            else:
                if (C>A) and (C>B) :
                    if A<B:
                        print "Valor C es mayor y Valor A es menor"
                    else:
                        print "Valor C es mayor y Valor B es menor"
        
