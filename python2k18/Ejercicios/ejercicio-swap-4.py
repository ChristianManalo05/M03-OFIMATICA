# coding: utf8
# Christian Mañibo
# 21/02/2018


# Variables
cajon1="movil"
cajon2="bocadillo"
cajon3="boli"
cajon4="bebida"

#Imprimimos las variables antes del cambio
print ""
print "ANTES"
print "Cajon 1 ----->", cajon1
print "Cajon 2 ----->", cajon2
print "Cajon 3 ----->", cajon3
print "Cajon 4 ----->", cajon4

cama=cajon1
cajon1=cajon3
cajon3=cama
cama=cajon4
cajon4=cajon2
cajon2=cama



#Imprimimos las variables despues del cambio
print ""
print "DESPUES"
print "Cajon 1 ----->", cajon1
print "Cajon 2 ----->", cajon2
print "Cajon 3 ----->", cajon3
print "Cajon 4 ----->", cajon4
