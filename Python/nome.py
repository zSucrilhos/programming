dicionario={"aeronave1":"Boeing 737-800 NG",
            "aeronave2":"Cessna 280 'Grand Caravan'",
            "aeronave3":"Sukhoi Su-35 'Flanker-E'",
            "aeronave4":"Boeing F-15E 'Eagle'",
            "aeronave5":"Dassault Mirage 2000-10",
            "aeronave6":"Dassault Rafale",
            "aeronave7":"Eurofighter 2000",
            "aeronave8":"Sukhoi Su-34 'Fullback'",
            "aeronave9":"Airbus A320",
            "aeronave10":"Airbus A340",
            "aeronave11":"Airbus A380",
            "aeronave12":"Boeing 747,400",
            "aeronave13":"Boeing 787-900 'Dreamliner'",
            "aeronave14":"Embraer Phenom 100"}

#Usar camelCase

import math
print("Digite o primeiro nome: " )
nome1=input()
print("Digite o segundo nome: ")
nome2=input()
print("Digite o terceiro nome: ")
nome3=input()
print("Digite o quarto nome: ")
nome4=input()
print("Os nomes digitados são %s %s %s %s" %(nome1+", ", nome2+", ", nome3+", e ", nome4))

print("Digite o nome da chave para procurar no dicionário: ")
valorChave=input()
resultado = 'valorChave' in dicionario
print(resultado)

print("ABACAXI")
nome = "abacaxi"
caracteristica = "amarelo"
numero=123456
pi=math.pi
xStrings="ABCDE"
print("%s é uma fruta" %(nome))
print("%s é %s %i" %(nome, caracteristica, numero))
print("O número pi é %.8f" %(pi))
print("É exibido somente as primeiras três letras da variável 'xStrings' (%s)" %(xStrings))
print("huiaaahull %.3s" %(xStrings))
print("Teste com o 'y' no marcador de strings")
print("%y
