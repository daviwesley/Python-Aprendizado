#!/usr/bin/env python
import math

def formulaHeron(a, b, c):
    # calcula o perimetro
    perimetro = a + b + c
    # calcula o semi-perimetro
    s = (a + b + c) / 2
    # calcula a area
    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    # imprime resultados
    print "\n O perimetro do triangulo = %.2f" %perimetro
    print " O semi-perimetro do triangulo = %.2f" %s
    print " A area do triangulo eh  %0.2f" %area

ladoA = int(input("Entre com o numero do lado A: "))
ladoB = int(input("Entre com o numero do lado B: "))
ladoC = int(input("Entre com o numero do lado C: "))

formulaHeron(ladoA, ladoB, ladoC)
