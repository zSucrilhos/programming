num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
while True:
    soma = float(num1+num2)
    multiplicacao = float(num1*num2)
    print("\nO que você gostaria de fazer? Use os números para selecionar a opção.")
    print("\n\t[1] - Somar\n\t[2] - Multiplicar\n\t[3] - Digitar novos números descartando os já digitados\n\t[4] - Sair do programa")
    escolha = int(input("Digite o número que corresponde à sua escolha: "))
    print('-'*80)
    if escolha == 1:
        print("\tSoma")
        print("{:.1f} + {:.1f} = {:.1f}".format(num1, num2, soma))
    elif escolha == 2:
        print("\tMultiplicação")
        print("{:.1f} x {:.1f} = {:.1f}".format(num1, num2, multiplicacao))
    elif escolha == 3:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        continue
    elif escolha == 4:
        break
    else:
        print("\n\tDigite apenas números.")
print("Até mais!")
