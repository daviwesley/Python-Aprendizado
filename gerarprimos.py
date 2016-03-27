#!usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Questão 2
Escreva uma função que receba um inteiro n e gere um lista com os n
primeiros numeros primos
'''

def gerarPrimos(numero):
    for primo in range(1,numero+1):
        if primo > 1:
            for i in range(2,primo):
                if (primo % i) == 0:
                    break
            else:
                print primo

primosInput = int(input("Entre com a quantidade de primos: "))

gerarPrimos(primosInput)
