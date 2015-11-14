#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
A declaração else complementa a declaração if. Um par if/else diz: 
"Se esta expressão for verdadeira, execute o bloco de código recuado; 
caso contrário, execute o código depois da declaração else."
'''

answer = "E so um arranhao!"

def black_knight():
    if answer == "E so um arranhao!":
        return True
    else:             
        return False       # Tenha certeza de que isso retorna False

def french_soldier():
    if answer == "Va embora, ou vou zombar de voce mais uma vez!":
        return True
    else:             
        return False       # Tenha certeza de que isso retorna False
