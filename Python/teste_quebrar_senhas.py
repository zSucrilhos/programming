senha_teste = 'vini'
letras_minusculas = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
                     'x','w','y','z')
fixa = 0
fixab = 0
senha = ''
while True:
    while True:
        for i in range(0,26):
            senha = letras_minusculas[fixa] + letras_minusculas[i]
            print(senha)
            if senha == senha_teste:
                print(f'senha encontrada: {senha}')
        for i in range(0,26):
            senha = letras_minusculas[fixa] + letras_minusculas[fixab] + letras_minusculas[i]
            print(senha)
            if senha == senha_teste:
                print(f'senha encontrada: {senha}')
        fixa = fixa + 1
    fixab = fixab + 1
