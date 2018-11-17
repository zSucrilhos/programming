# Importando sleep() e randint()
from time import sleep
from random import randint

# Declaração das variáveis
produto = str()
preco = float()
random1 = randint(0, 100)
random2 = randint(0, 100)
random3 = randint(0, 100)
random4 = randint(0, 100)
random5 = randint(0, 100)
random6 = randint(0, 100)
random7 = randint(0, 100)
random8 = randint(0, 100)
random9 = randint(0, 100)
random10 = randint(0, 100)
pag_cond = int()
desconto_produto = float()
desconto_final = float()
parcelas = float()


print("BEM VINDO A ERICK'S SHOP!!")
print(
    "AGORA VAMOS FAZER O SEU CHECK-OUT! SINTA-SE À VONTADE E SIGA AS INSTRUÇÕES NA TELA")
print()
print("PROMOÇÃO DE NATAL! OFERECEMOS 10% DE DESCONTO EM QUALQUER PRODUTO DA LOJA! APROVEITE!")
print()
# Colhendo informações do usuário
produto = str(input("Qual o produto comprado na loja? "))
produto = produto.title()
preco = input("Digite o preço do produto: ")
if preco <= 0 or type(preco) != float:
    print("Desculpe, mas parece que você digitou um número errado, não?")
# Aqui o programa deveria requisitar ao usuário a entrada do valor novamente.
elif preco > 0:
    print()
    print(
        "Qual a condição de pagamento?\n\t1 - À VISTA - 10% de desconto!\n\t2 - NO CARTÃO - 5% de desconto\n\t3 - ATÉ 2X NO CARTÃO - Preço normal\n\t4 - 3X OU MAIS - 20% de juros!"
    )
    print("\n\t\t*Nós não aceitamos cheques")
    pag_cond = int(input("... : "))
    # Sleep em ação!
    # If/Else aninhados
    if pag_cond == 1:
        print("\nCalculando o seu desconto, aguarde!")
        sleep(1)
        print("X²+{}•{}".format(random2, random5))
        sleep(1)
        print("∆=b²-4•{}•{}".format(random2, random4))
        sleep(1)
        print(
            "{}³ x {} - 1 √{}³/{}...".format(
                random1, random2, random3, random4
            )
        )
        sleep(1)
        print(
            "{} x {} + {} x {} / {}".format(
                random5, random6, random9, random10, random1
            )
        )
        # Calculando o desconto de 10%
        desconto_produto = float(preco * 0.1)
        desconto_final = float(preco - desconto_produto)
        print(
            "Ok, o seu pagamento é à vista, o total fica R$: {:.2f} x {:.2f} √{} + {} x {} + 10%".format(
                preco, random1, random5, random7, random10
            )
        )
        sleep(1)
        print("\tEntão, o valor final é de R$ {:.2f}".format(desconto_final))
        print()
        print("Você já pode levar o seu {} para casa!".format(produto))
        print("Obrigado pela compra, volte sempre, estaremos aguardando!!!")
        print(
            "A saída é por ali >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 'EXIT' "
        )
    elif pag_cond == 2:
        print("\nCalculando o seu desconto, aguarde!")
        sleep(1)
        print("X²+{}•{}".format(random2, random5))
        sleep(1)
        print("∆=b²-4•{}•{}".format(random2, random4))
        sleep(1)
        print(
            "{}³ x {} - 1 √{}³/{}...".format(
                random1, random2, random3, random4
            )
        )
        sleep(1)
        print(
            "{} x {} + {} x {} / {}".format(
                random5, random6, random9, random10, random1
            )
        )

        # Calculando o desconto de 5%
        desconto_produto = float(preco * 0.05)
        desconto_final = float(preco - desconto_produto)
        print("Ok, o seu pagamento é à vista no cartão, o total fica R$: ")
        sleep(1)
        print(
            "{:.2f} ∑ {} ≤{} + {} x {} + 10%".format(
                preco, random5, random2, random6, random9
            )
        )
        sleep(1)
        print("\tO preço final é de R$ {:.2f}".format(desconto_final))
        print()
        print("Você já pode levar o seu {} para casa!".format(produto))
        print()
        print("Obrigado pela compra, volte sempre, estaremos aguardando!!!")
        print(
            "A saída é por ali >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 'EXIT' "
        )
    elif pag_cond == 3:
        print("\nCalculando o seu desconto, aguarde!")
        sleep(1)
        print("X²+{}•{}".format(random2, random5))
        sleep(1)
        print("∆=b²-4•{}•{}".format(random2, random4))
        sleep(1)
        print(
            "{}³ x {} - 1 √{}³/{}...".format(
                random1, random2, random3, random4
            )
        )
        sleep(1)
        print(
            "{} x {} + {} x {} / {}".format(
                random5, random6, random9, random10, random1
            )
        )

        # Calculando o valor das parcelas
        parcelas = float(preco / 2)
        print("Ok, o seu pagamento é em 2X no cartão, o total fica R$: ")
        sleep(1)
        print(
            "{:.2f} ∑ {} √{} x {} - {}".format(
                preco, random5, random7, random8, random9
            )
        )
        sleep(1)
        print("\tEntão, o total fica R$ {:.2f}".format(parcelas))
        print()
        print("Você já pode levar o seu {} para casa!".format(produto))
        print("Obrigado pela compra, volte sempre, estaremos aguardando!!!")
        print(
            "A saída é por ali >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 'EXIT' "
        )
    elif pag_cond == 4:
        print("\nCalculando o seu desconto, aguarde!")
        sleep(1)
        print("X²+{}•{}".format(random2, random5))
        sleep(1)
        print("∆=b²-4•{}•{}".format(random2, random4))
        sleep(1)
        print(
            "{}³ x {} - 1 √{}³/{}...".format(
                random1, random2, random3, random4
            )
        )
        sleep(1)
        print(
            "{} x {} + {} x {} / {}".format(
                random5, random6, random9, random10, random1
            )
        )

        # Número de parcelas
        parcelas = int(input("Digite o número de parcelas: "))
        sleep(1)
        print(
            "Ok, o seu pagamento é em 3X ou mais no cartão, o total fica R$: "
        )
        sleep(1)
        print(
            "{:.2f} ∑ ^{} √{} x {} - {}".format(
                preco, random7, random2, random1, random8
            )
        )
        sleep(1)
        # Calculando o valor das parcelas
        preco_parcelas = float(preco / parcelas)
        print(
            "\tEntão, o total ficou R$ {:.2f} e você paga em apenas diminutas {} parcelas.".format(
                preco_parcelas, parcelas
            )
        )
        print()
        print("Você já pode levar o seu {} para casa!".format(produto))
        print("Obrigado pela compra, volte sempre, estaremos aguardando!!!")
        print(
            "A saída é por ali >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 'EXIT' "
        )
    elif pag_cond > 4:
        print("Por favor, digite uma opçãó válida.")
    else:
        print("Desculpe, não entendi.")
else:
    print("Por favor digite um valor válido!")
