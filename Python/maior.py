# -*- coding: utf8 -*-
print('Este programa deteca se o número é positivo, negativo ou igual a zero')
while True:
    num = int(input('Digite um número: '))
    if num == 0:
        print('O número é igual a zero!')
    elif num < 0:
        print('Este é um número negativo!')
    elif num > 0:
        print('Este é um número positivo!')
    print()
    continue
