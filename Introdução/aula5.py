#!/usr/bin/env pyton

#comentarios com multiplas linhas usa-se o """ no inicio e final

"""
formata e exibe no console o valor de total com exatamente 
dois numeros depois da virgula 
"""
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total=meal + meal * tip

print("%.2f" % total)
