# -*-	coding: utf8 -*-

#1) Escreva uma funcao que retire as duplicatas de uma lista dada como argumento
#	>>> Duplicata ([1,2,2,3,3,3,4,4,4,4])
#	>>> [1,2,3]
	
def remove_dup(lista, i = 0):
	if len(lista) == 0 or len(lista) == i:
		return []
	lista.sort()
	if i + 1 < len(lista) and lista[i] == lista[i + 1]:
		return remove_dup(lista, i + 1)
	return [lista[i]] + remove_dup(lista, i + 1)
	
x = [1,2,2,3,3,3,4,4,4,4]
print remove_dup(x)
	

#2) Defina uma funcao que calcule todos os divisores proprios de um numero(todos os divisores exeto o proprio numero)
#	>>>div_prop(15)
#	>>>[1,3,5]

def div_prop(n, div = 1):
	if n == 0:
		return []
	if n == div:
		return []
	if n % div == 0:
		return [div] + div_prop(n, div + 1)
	return div_prop(n, div + 1)

print div_prop(0)

#3) Um numero inteiro se diz perfeito se for igual a soma de divisores proprios. Escreva funções para:
#	a)Verificar se um numero n eh perfeito

def div_propS(n, div = 1):
	if n == 0:
		return 0
	if n == div:
		return 0
	if n % div == 0:
		return div + div_propS(n, div + 1)
	return div_propS(n, div + 1)
def is_perfect(n):
	if n == div_propS(n):
		return "É perfeito"
	return "Não perfeito"

print is_perfect(6)



#	b)Gerar uma lista dos primeiros numeros perfeitos(n eh argumento da funcao)

#4)Defina uma funcao que receba um numero inteiro positivo < 1000 e retorne sua string com numero por extenso 
#	>>>extenso(42)
#	>>>"quarenta e dois"

#5) A constante matematica (pi) pode ser aproximada pela serie

#		(pi)² / 12 = (somatorio)(-1)^k / (k + 1)²
#-Escreva uma funcao para aproximar o valor de (pi) somando k parcelas da serie acima, K eh argumento da funcao		  
#
