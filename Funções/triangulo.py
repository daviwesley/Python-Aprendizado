#!/usr/bin/env python

def verificaTriangulo(a, b , c):
    if a == b and b == c and a == c:
        print 'forma um triangulo'
    else:
        print 'nao formam um triangulo'

ladoA = int(input("Entre com o numero do lado A: "))
ladoB = int(input("Entre com o numero do lado B: "))
ladoC = int(input("Entre com o numero do lado C: "))

verificaTriangulo(ladoA, ladoB, ladoC)
