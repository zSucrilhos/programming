numeros = []
c = 0
while True:
    num = int(input('Digite um número: '))
    c += 1
    numeros.append(num)
    print(f'O número que você digitou foi {num}.')
    print('\tDigite "999" para parar.\n')
    if num == 999:
        c -= 1
        del numeros[-1]
        soma = sum(numeros)
        break
if c > 1:
    print(f'Você digitou {c} números e a soma deles foi {soma}.')
    print(f'Foram eles {numeros}.')
elif c == 1:
    print(f'Você digitou {c} número.')
