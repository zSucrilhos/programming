while True:
    # idade = 0
    idade = int(input("Digite a sua idade: "))
    if idade <= 2:
        print('Você é um bebê!')
    elif idade > 2 and idade <= 4:
        print('Você é uma criança!')
    elif idade > 4 and idade <= 13:
        print('Você é um garoto(a)!')
    elif idade > 13 and idade < 20:
        print('Você é um adolescente!')
    elif idade >= 20 and idade < 65:
        print('Você é um adulto!')
    elif idade >= 65:
        print('Você é um idoso!')