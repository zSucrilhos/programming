# -*- coding: utf-8 -*-
import time
# Ingredientes das pizzas:
ingredientes_Naturale = ['Mussarela de búfala ralada','Mussarela de búfala ralada',\
'Tomate picado','Espinafre','Abobrinha','Berinjela','Alho poró','Azeitona preta',\
'Manjericão fresco']
ingredientes_4Queijos = ['Mussarela','Provolone','Parmesão','Catupiry']
ingredientes_Prima_De_Parma = ['Mussarela','Presunto de Parma','Pesto de manjericão',\
'Lascas de parmesão']
ingredientes_Blumenau = ['Molho parmegiana','Mussarela','Linguiça Blumenau',\
'Manjericão fresco']

pizzas = {'Naturale':ingredientes_Naturale, '4Queijos':ingredientes_4Queijos,\
'Prima de Parma':ingredientes_Prima_De_Parma, 'Blumenau':ingredientes_Blumenau}


print('Bem-vindo à pizzaria do Erick\nEm que posso ajudar?')
print('\n\t[1] - Cardápio\n\t[2] - Sair do programa\n\t')
opcao = str(input('\t>>> '))
c = 0
while True:
    if opcao == '1':
        print(f'{"PIZZAS": >16} | {"INGREDIENTES": >13}')
        for pizza, ingredientes in pizzas.items():
            c += 1
            print(f'{[c]}, {pizza: <15} = {ingredientes}')
        print('\nQual pizza você vai querer? ')
        pizza_escolha = input('\t>>> ')
        print(f'A pizza que você escolheu foi: {pizza_escolha[c]}')
        break
    elif opcao == '2':
        print('Até mais!\n*encerrando o programa*')
        time.sleep(3)
        break
    else:
        print('Por favor, digite uma opção válida!')
        continue
