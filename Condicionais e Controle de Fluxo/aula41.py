#!/usr/bin/env python
# -*- coding: UTF-8 -*-

pyg = 'ay'

original = raw_input('Insira uma palavra:')

if len(original) > 0 and original.isalpha():
    #transforma a string em minúscula	
    word = (original.lower())
    first = word[0]#pega a primeira letra da palavra
    new_word = word+first+pyg#junta tudo
    print new_word[1:len(new_word)]#imprime da segunda palavra até o resto da string
else:
    print 'empty'
