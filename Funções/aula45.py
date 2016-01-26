#!/usr/bin/env python

'''
Funções Chamando Funções
Vimos funções que podem exibir texto ou realizar aritimética simples,
mas as funções podem ser muito mais poderosas do que isso. Por exemplo,
uma função pode chamar outra função:
'''

def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2
