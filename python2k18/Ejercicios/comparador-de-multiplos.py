# coding:utf8
# Christian Mañibo
# 23/02/2018

import os
os.system("clear")

print"""

*********************************************

            COMPARADOR DE MULTIPLES

*********************************************
"""


num1=input("Escriba un número: ")
num2=input("Escriba otro número: ")

print "#RESPUESTA#"
if (num1==0) or (num2==0):
    print "No es posible con ceros."
elif (num1>num2) :
	
   if (num1%num2==0):
       print num1, "es múltiplo de" , num2
       
   else:
	   
       print num1, "no es múltiplo de", num2
       
elif (num2>num1):
	
   if (num2%num1==0):
       print num2, "es múltiplo de" , num1
       
   else:
       print num2, "no es múltiplo de", num1
       
else:
    print "Son iguales." , num1, "es múltiplo de" , num2
