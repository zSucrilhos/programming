# -*- coding: utf-8 -*-
def fatorial():
    """ Retorna o fatorial de um número n """
    n = int(input('Digite um número: '))
    if n == 1:
        return 1
    else:
        x = n+1
        for i in range(0,n):
            x = n-1
            f = n*x
            print(f'x é {x}')
            print(f'f é {f}')

if __name__ == '__main__':
    fatorial()
