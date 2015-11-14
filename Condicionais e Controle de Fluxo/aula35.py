#!/usr/bin/env python
# -*- coding: UTF-8 -*-
pyg = 'ay'
original = raw_input('Digite uma palavra:')
if len(original) > 0 and original.isalpha():
   word = original.lower()#deixa tudo minúsculo
   first = word[0]#pega a primeira letra da palavra
   new_word = word + first + pyg#junta tudo
   #pega a segunda letra e imprime o resto
   new_word = new_word[1:len(new_word)]
   print new_word
else:
    print 'empty'
