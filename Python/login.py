# -*- coding: utf-8 -*-
a = 'Formulário de Login, "LogForm v0.3"'
print(f'{a:^59}')
print('#'*59)

usuarios = []
senhas = []

def new_usr():
	usr_name = str(input('Novo nome de usuário: '))
	usuarios.append(usr_name)

	usr_psw = str(input('Nova senha: '))
	senhas.append(usr_psw)

def login():
		print('Digite o seu nome de usuário: ')
		username_input = str(input('\t>>> '))
		print('Digite a sua senha:')
		usr_psw_input = str(input('\t>>> '))
		if username_input in usuarios and usr_psw_input in usuarios:
			print('Você está logado!')
			print('>>> ')
			break
		elif username_input in usuarios and usr_psw_input not in usuarios:
			print('A sua senha está errada, tente novamente')
			continue
		elif username_input not in usuarios and usr_psw_input in usuarios:
			print('O seu nome de usuário está errado, tente novmante')
			continue
		elif username_input not in usuarios and usr_psw_input not in usuarios:
			print('Credenciais inválidas, tente novamente.')
			continue


while True:
	if not usuarios:
		print('Não há usuários registrados anteriormente.\nRegistre um novo usuário!\n')
		print('Registrar novo usuário?\n\t1 - SIM\n\t2 - NÃO\n\t')
		se = str(input('>>> '))
		if se == '1':
			new_usr()
			print('Usuário registrado com sucesso!')
			print()
			print(usuarios)
			print(senhas)
			break
		elif se == '2':
			print('O programa encerrará!')
			break
		else:
			print('Por favor, digite uma opção válida!\n\n\n')
			continue
		login()
