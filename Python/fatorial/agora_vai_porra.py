# -*- coding: utf-8 -*-
def fatorial(n):
    """ Retorna o fatorial de um número n """
    if n == 1:
        return 1
    else:
        for c in range(n, 0+1, -1):
            c -= 1
            n = n*c
        return n
if __name__ == '__main__':
    n = int(input('num: '))
    fatorial(n)
