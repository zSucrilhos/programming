from time import sleep
###########################
nome = input("Digite o seu nome: ")
nome = nome.title()
print("Olá %s" %(nome))
print("O serviço de alistamento obrigatório informa que você deve se alistar até Novembro do ano em que completa 18 anos.")
print()

ano_atual = int(2018)
doze_meses = int(12)
dia_nascimento = int(input("Digite o dia do seu nascimento: "))
mes_nascimento = int(input("Digite o mês do seu nascimento: "))
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
idade_canditato = int(ano_atual-ano_nascimento)
falta_ano_alistamento = int(ano_atual-idade_canditato)

mes_alistamento = int(11)
falta_mes_alistamento = mes_alistamento-mes_nascimento

if idade_canditato < 18:
    print("Ainda falta %i ano e %i mês para o prazo de alistamento vencer. Lembre-se de suas obrigações como cidadão!" %(falta_ano_alistamento, falta_mes_alistamento))
    if falta_ano_alistamento > 1:
        print("Ainda faltam %i anos e %i meses para o prazo de alistamento vencer. Lembre-se de suas obrigações como cidadão!" %(falta_ano_alistamento, falta_mes_alistamento))
elif idade_canditato == 18:
    print("Você está em cima do prazo para se alistar! Procure o quartel mais próximo com seus documentos em mãos!")
else:
    print("O prazo para o alistamento venceu!")

