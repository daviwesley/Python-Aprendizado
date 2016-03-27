#!/usr/bin/env python

import math

def calcularBhaskara(a, b , c):
    d=(b^2)-(4*a*c)
    if d<0 :
            print ("Delta negativo, raiz impossivel de ser extraida.")
    else :
        print "Delta: %s." % d
        m1=math.sqrt(d)
        x1=(-b+m1)/(2*a)
        x2=(-b-m1)/(2*a)
        print "Raiz ~ X1= %s." % x1
        print "Raiz ~ X2= %s." % x2


cA = int(input("Entre com o coeficiente a: "))
cB = int(input("Entre com o coeficiente b: "))
cC = int(input("Entre com o coeficiente c: "))

print str(cA) + "*" + "x" + "+" + str(cB) + "*" + "+" + str(cC) + "= 0"

calcularBhaskara(cA, cB, cC)
