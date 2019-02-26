# função fatorial com recursividade

fat = lambda x: x == 0 and 1 or x * fat(x-1)
fat(9)
