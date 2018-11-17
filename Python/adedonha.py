import random
from time import sleep
pc_choice = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
choice = random.choice(pc_choice) #Escolhe uma letra da lista
animal = 0
cidade = 0
carro = 0
marca = 0
correção_pontuação = 0
pontuação = 0
print('='*50)
print('A LETRA ESCOLHIDA FOI >> {} <<'.format(choice))
print('=' * 50)

###################################################################

cidade = str(input('Digite o nome de uma cidade! '))

while cidade[0] != choice:
    print ('='*50)
    cidade = str(input('Parece que a cidade que você escreveu não começa com a letra "{}". Digite o nome de uma cidade válida para essa rodada! '.format(choice)))


animal = str(input('Digite o nome de um animal! '))

while animal[0] != choice:
    print ('='*50)
    animal = str(input('Parece que o animal que você escreveu não começa com a letra "{}". Digite o nome de um animal válido para essa rodada! '.format(choice)))



marca = str(input('Digite o nome de uma marca! '))
while marca[0] != choice:
    print ('='*50)
    marca = str(input('Parece que a marca que você escreveu não começa com a letra "{}". Digite o nome de uma válida para essa rodada! '.format(choice)))


carro = str(input('Digite o nome de um carro: '))

while carro[0] != choice:
    print ('='*50)
    carro = str(input('Parece que o carro que você escreveu não começa com a letra "{}". Digite o nome de um carro válido para essa rodara!' .format(choice)))
print ('='*50)
print('A cidade é: {}\nO animal é: {}\nA marca é: {}\nO carro é: {}'.format(cidade,animal, marca, carro))

print ('='*50)
correção_pontuação_cidade = str(input('A cidade que você escolheu, foi a mesma de alguém? [S/N] ')).upper().split()

if correção_pontuação_cidade == 'S':
    correção_pontuação = 5
else:
    correção_pontuação = 10
print('Você está com {} pontos.'.format(correção_pontuação))
print ('='*50)
correção_pontuação_animal = str(input('O animal que você escolheu, foi o mesmo de alguém? [S/N] ')).upper().split()

if correção_pontuação_animal == 'S':
    correção_pontuação += 5
else:
    correção_pontuação += 10
print('Você está com {} pontos.'.format(correção_pontuação))
print ('='*50)
[teste1 teste1 teste1, ]

correção_pontuação_carro = str(input('O carro que você escolheu, foi o mesmo de alguém? [S/N] ')).upper().split()

if correção_pontuação_carro == 'S':
    correção_pontuação += 5
else:
    correção_pontuação += 10

print('Você está com {} pontos.'.format(correção_pontuação))


print('='*50)
correção_pontuação_marca = str(input('A marca que você escolheu, foi a mesma de alguém? [S/N] ')).upper().split()
print ('='*50)
if correção_pontuação_marca == 'S':
    correção_pontuação += 5
else:
    correção_pontuação += 10

print('Você está com {} pontos.'.format(correção_pontuação))

print ('='*50)
print('A sua pontuação foi de {}'.format(correção_pontuação))
