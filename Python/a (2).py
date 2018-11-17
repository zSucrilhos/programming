# -*- coding: utf-8 -*-
import random
import time
print('-'*100)
print('Você está no mundo de samuelândia e agora enfrentará uma grande aventura pela frente! Boa jornada!')
print('-'*100)
time.sleep(0.5)
sexo= ''
classe = (0,'Caveleiro', 'Guerreiro', 'Mago', 'Arqueiro')
escolha_classe = 0
classe_atributos = 0
classe_info = 0
while True:
    sexo= str(input('Você deseja ser homem ou mulher?\n\tM - Masculino\n\tF - Feminino\n>>>\t')).upper().strip()[0]
    print('Analizando...')
    time.sleep(1)
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Ops, Parece que você não digitou um sexo válido!')
        time.sleep(0.5)
if sexo == 'M':
    print('>>>\tMuito prazer cavalheiro.')
    time.sleep(1)
if sexo == 'F':
    print('>>>\tMuito prazer bela dama.')
    time.sleep(1)
print(f'>>>\tBom, para começar a jornada você precisa escolher uma classe, qual é a sua preferida?\n\t1 - CAVALEIRO\n\t2 - GUERREIRO\n\t3 - MAGO\n\t4 - Arqueiro')
while True:
     if classe_atributos == 'N':
         break
     if classe_atributos != 'S':
        classe_atributos = str(input('Deseja saber as características de cada classe? [S/N]')).upper().strip()[0]
     time.sleep(0.5)
     if classe_atributos == 'N':
         break
     elif classe_atributos == 'S':
         classe_info = int(input('Qual classe deseja saber as características?\n\t1 - CAVALEIRO\n\t2 - GUERREIRO\n\t3 - MAGO\n\t4 - Arqueiro'))
         if classe_info == 1:
            print(f'{classe[1]:.^100}')
         elif classe_info == 2:
            print(f'{classe[2]:.^100}')
         elif classe_info == 3:

            print(f'{classe[3]:.^100}')
         elif classe_info == 4:
            print(f'{classe[4]:.^100}')
         else:
            print('Parece que esta classe não está no catálogo :/')
     else:
         print('Responda somente com SIM ou NÃO.')
     classe_atributos = str(input('Deseja saber as características de mais alguma classe? [S/N]')).upper().strip()[0]
     if classe_atributos != 'S' or classe_atributos != 'N':
        while True:
            classe_atributos = str(input('Digite somente sim ou não. Deseja saber as características de mais alguma classe? [S/N]')).upper().strip()[0]
            if classe_atributos == 'S' or classe_atributos == 'N':
                break


    
escolha_classe = str(input('>>>\tEu escolho a classe '))
print('Analizando...')
time.sleep(1)


if int(escolha_classe) > 4 or int(escolha_classe) < 1:
    while True:
        escolha_classe = str(input('>>>\tPor favor digite uma classe válida! Qual a classe que você escolhe? '))
        print('Analizando...')
        time.sleep(1)
        if int(escolha_classe) > 0 and (escolha_classe) < 5:
            break
if escolha_classe == '1':
    print(f'A partir de agora você é um {classe[1]}!')
elif escolha_classe == '2':
    print(f'A partir de agora você é um {classe[2]}!')
elif escolha_classe == '3':
    print(f'A partir de agora você é um {classe[3]}!')
elif escolha_classe == '4':
    print(f'A partir de agora você é um {classe[4]}!')
else:
    print('Parece que temos um problemas, vamos corrigir em breve.')
