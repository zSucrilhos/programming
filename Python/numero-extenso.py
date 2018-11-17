numeros_extenso = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    usr_num = int(input("Digite um número inteiro entre 0 e 20: ").strip())
    if usr_num < 0 or usr_num > 20:
        print("\tVocê digitou um número diferente do intervalo especificado, digite apenas números entre 0 e 20.\n")
        continue
    print(f'Você digitou o número {numeros_extenso[usr_num]}\n')
