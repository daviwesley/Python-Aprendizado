#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Um numero primo eh um numero natural maior do que 1
que tem apenas dois divisores positivos distintos, 1 e ele mesmo
'''
__author__      = "Davi Wesley"
__email__ = "davi.wesley@icloud.com"

def verificaPrimos(num):
    # numeros primos sao maiores do que 1
    if num > 1:
       # cria um laço para verificar o divisor
       # se houver um divisor antes do numero informado
       # sabemos esse numero nao eh um primo :)
       for i in range(2,num):
           if (num % i) == 0:
               print num,"nao eh um numero primo"
               break
       else:
           print num,"eh um numero primo"
    # se o numero informado e menor que
    # ou igual a 1, nao e um numero primo
    else:
        print num,"nao eh numero primo"

num = int(input("Entre com um numero: "))
verificaPrimos(num)
