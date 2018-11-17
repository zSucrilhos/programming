#-*- coding: utf8 -*-
from time import sleep
admin_login = {'login':'admin', 'senha':'admin'}
print('#'*100)
login = 'SYSTEM login'
print(f'{login:^100}')
login_attempt = int(0)
print('SYSTEM login form v0.3 - Copyright 2018, Erick César')
print('\nVocê deseja se logar ou criar um novo usuário?\n')
print('1 - LOGAR\n2 - CRIAR NOVO USUÁRIO')
choice_login = str(input('\n>>> ').strip())[0]
if choice_login == '1':
    while True:
        if login_attempt >= 3:
            print('Você já pode tentar novamente!')
        usr_login = str(input('\nLogin: ')).strip()
        usr_psw = str(input('Senha: ')).strip()
        print('#'*100)
        if usr_login != admin_login['login'] or usr_psw != admin_login['senha']:
            print('Dados informados são inválidos. Por favor tente novamente.')
            login_attempt += 1
            left_attempts = 3 - login_attempt
            print(f'Você ainda tem {left_attempts:02} tentativas para se logar.')
            while login_attempt >= 3:
                print('Você excedeu o número máximo de tentativas, tente novamente em 20 segundos.')
                for c in range(20, -1, -1):
                    print(c, end=' ', flush=True) # Consultar sobre o 'flush=True'
                    sleep(1)
                continue
            continue
        elif usr_login == admin_login['login'] and usr_psw == admin_login['senha']:
            print(f'Logado com sucesso! Bem vindo, {usr_login}!')
            break
elif choice_login == str(2):
    print('new_usr = {input('')')
    print('O programa ainda está em alpha!')
