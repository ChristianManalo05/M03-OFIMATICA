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
