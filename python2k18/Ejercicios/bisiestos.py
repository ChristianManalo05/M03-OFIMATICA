# coding:utf8
# Christian Mañibo
# 28/02/2018


import os
os.system ("clear")

print """

**************************************************
           
           COMPROBADOR DE AÑOS BISIESTOS

**************************************************

"""
anyo=input("Escriba un año y le diré si es bisiesto: ")

if anyo==0:
   print "No hubo año 0"
else:
    if anyo%400==0:
       print anyo,"es año bisiesto"
    
    
    else:
	
        if anyo%4==0:

            if anyo%100!=0:
                print anyo,"es año bisiesto"
	
            else:
                print anyo,"no es año bisiesto"
        else:
            print anyo, "no es año bisiesto"
