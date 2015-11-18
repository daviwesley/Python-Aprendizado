#!/usr/bin/env python
# -*- coding: UTF-8 -*-

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
	#transforma a string em minúscula	
    word = (original.lower())
    first = word[0]#pega a primeira letra da palavra
    print original
else:
    print 'empty'
