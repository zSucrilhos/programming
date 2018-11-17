palavras = ('carro','moto','veiculo','hercules','aviao','computador','bicicleta',
'processador','compiuter','placa','mae')
for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} contém as seguintes vogais: ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
