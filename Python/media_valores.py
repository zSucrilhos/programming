# Esse programa pede ao usuário para digitar vários números em sequência e depois
# calcula a média o maior número e o menor número.
#################################################################################

# Inicialização das variáveis
exit_loop = ''
numeros = []
num = 0
n_soma = 0
n_min = 0
n_max = 0
n_media = 0
qtde = 0
continuar = ''
c = 0

#################################################################################
# Início do loop
while True:
    num = int(input('Digite um número: '))
#     if type(num) is not int:
#         print('Por favor, digite apenas NÚMEROS')
#         continue
    numeros.append(num)
    c += 1
    print(f'O número adicionado foi {num}.')
    continuar = input('\n\tContinuar adicionando números? [S/N]: ').lower().strip()[0]
    if continuar == 's':
        continue
    elif continuar == 'n':
        break
    else:
        print("Por favor, digite uma opção válida.")
        continue
n_soma = sum(numeros)
n_min = min(numeros)
n_max = max(numeros)
qtde = len(numeros)
print('Os números adicionados foram: ')
print(*numeros, sep=', ')
print(f'\tE o total de números digitados foi de {c} números.')
print(f'\tA soma dos números foi de {sum(numeros)}. O menor número foi {min(numeros)} e o maior foi {max(numeros)}.')
n_media = n_soma/qtde
print(f'A média de todos os númreros adicionados foi de {n_media}')
