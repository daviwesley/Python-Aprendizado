def func(arg):
    return arg + 2

lista = [2, 1, 0]

list(map(func, lista)) == [4, 3, 2] # true
