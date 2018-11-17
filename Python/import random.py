import random

dano_armas_principal_ = random.randint(20, 40)
player = {
    'nome': 'Erick', 'hp': 100, 'raca':'Nórdico',
}
# while True:
inventario = {
    'itens': {
        'hp_potion': 5,
        'flechas': 21,
        'tomo_feitico-fireball': 1,
    },
    'armas': {
        'principal': {
            'nome':'Espada de Aço Forjado',
            'estado':100,
            'dano': lambda: random.randint(4,9),
            },
        'secundaria': {
            'nome':'Adaga de Aço Polido',
            'estado':100,
            'dano': random.randint(2,5),
            },
        'ranged': {
            'principal':'Arco de Caça Reforçado',
            'estado':100,
            'dano':23,

            }
    },
    'armadura': {
        'cabeca': {
            'nome':'Elmo de Aço',
            'estado':100,
            'defesa':15,
            },
        'peitoral': {
            'nome':'Peitoral de Ferro',
            'estado':100,
            'defesa': 25,
            },
        'calca': {
            'nome':'Calças de Lã',
            'estado':100,
            'defesa':15,
            },
        'botas': {
            'nome':'Chinelo de Dedo',
            'estado': 100,
            'defesa': 10,
            }
    },
    'mochila': {
        'lanterna': {
            'duracao':67,

        }
    }
}

while True:
    print('\nAtacar?')
    print('\t1 - SIM\n\t2 - NÃO')
    attack = str(input('>>> '))
    if attack == '1':
        print('Atacando')
        print(f'Você deu {inventario["armas"]["principal"]["dano"]()} de dano no \
inimigo!')
        # enemy['hp'] -= arma['dano']
        # if enemy['hp']<= -1:
        #     print()
        # else:
        #     print(enemy['hp'])
        # if enemy['hp'] <= 0:
        #     print('Parabéns! Você venceu!')
        #     break
    # elif attack == '2':
    #     print('Round do inimigo!')
    #     print('O inimigo te deu 8 de dano!')
    #     player['hp'] -= 8
    #     print(f'O seu HP atual é: {player["hp"]}')
    #     if player['hp'] <= 0:
    #         print('Oh não! Você morreu! :/')
    #         break
    else:
        print('Por favor, digite uma opção válida!')
