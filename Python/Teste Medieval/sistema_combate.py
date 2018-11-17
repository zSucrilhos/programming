player = {'hp': 100, 'nome': 'Erick'}
enemy = {'hp': 100, 'nome': 'Goblin'}
arma = {'principal': 'Espada de Cristal', 'dano': 24}
while True:
    print('\nAtacar?')
    print('\t1 - SIM\n\t2 - NÃO')
    attack = str(input('>>> '))
    if attack == '1':
        print('Atacando')
        print(f'Você deu {arma["dano"]} de dano no inimigo!')
        enemy['hp'] -= arma['dano']
        print(enemy['hp'])
        if enemy['hp'] <= 0:
            print('Parabéns! Você venceu!')
            break
    elif attack == '2':
        print('Round do inimigo!')
        print('O inimigo te deu 8 de dano!')
        player['hp'] -= 8
        print(f'O seu HP atual é: {player["hp"]}')
        if player['hp'] <= 0:
            print('Oh não! Você morreu! :/')
            break
    else:
        print('Por favor, digite uma opção válida!')
