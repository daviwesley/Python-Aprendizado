#!/usr/bin/env python

print 'Bem-vindo ao Tradutor de Pig Latin!'
'''
Agora sabemos que temos uma string com conteúdo. Vamos ser ainda mais detalhistas.
Usando a função .isalpha você pode saber se somente letras na string.
'''
# Comece seu codigo aqui!
original = raw_input("Insira uma palavra")

#verifique se nao eh vazio e tem letras
if len(original)>0 and original.isalpha():
    print (original)
else:
    print ("Vazio")

