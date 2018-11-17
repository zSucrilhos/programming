t = []
vez = ['primeiro','segundo','terceiro','quarto']
for temp in range(0,4):
        temp += 1
        add = int(input(f'Digite o {vez[temp-1]} número: '))
        t.append(add)
print(f'O valor 9 apareceu {t.count(9)} vezes.')
if 3 not in t:
    print('O número 3 não apareceu em nenhuma posição')
if 3 in t:
    print(f'O número 3 foi digitado na posição {t.index(3, 0) + 1}')
    if t.count(3) > 1 and t.count(3) < 3:
        print(f'O número 3 foi digitado nas posiçoes {t.index(3, 1) + 1} e {t.index(3, 2) + 1}')
    elif t.count(3) > 3 and t.count(3) < 4:
        print(f'O número 3 foi digitado nas posições {t.index(3, 1) + 1}, {t.index(3, 2) + 1} e {t.index(3, 3) + 1}')
    elif t.count(3) == 4:
        print(f'O número 3 foi digitado nas posições {t.index(3, 1) + 1}, {t.index(3, 2) + 1}, {t.index(3,3) + 1} e {t.index(3, 4) + 1}')
print('\nOs números pares foram: ', end=' ')
for par in t:
    if par%2 == 0:
        print(par, sep=', ', end=' ')
print()
t = tuple(t)
print(t)