senha_teste = 'vini'
letras_minusculas = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
                     'x','w','y','z')
fixa = -1
cont = -1
senha = ''
tentativa = 0
while True:
    fixa = fixa + 1
    for i in range(0, 26):
        senha = letras_minusculas[fixa] + letras_minusculas[i]
        print(senha)
        tentativa = tentativa + 1
        if senha != senha_teste and tentativa == 676:
            fixa = 0
            i = -1
            while True:
                cont = cont + 1
                while 1==1:
                    i = i+1
                    senha = letras_minusculas[fixa] + letras_minusculas[cont] + letras_minusculas[i]
                    print(senha)
                    if senha == 'azz':
                        fixa = fixa + 1
                    if i == 26:
                        i = 0





        elif senha == senha_teste:
            print(f'A senha é: {senha}')
            break
