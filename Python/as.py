from time import sleep
produto= float(input('Quanto custou o produto?\n\t'))
pagamento = str(input('''Digite a forma de pagamento:\n\t------------------------------------------------\n\t1 -- dinheiro / chueque: 10% de desconto\n\t------------------------------------------------\n\t2 -- A vista no cartão: 5% de desconto\n\t------------------------------------------------\n\t3 -- 2X no cartão: Preço normal\n\t------------------------------------------------\n\t4 -- 3X ou mais no cartão: 20% de juros!\n\t------------------------------------------------\n\t\n\t'''))
print('\n\tAnalisando...')
sleep(1)
desc_5 = produto - produto * 0.05
if pagamento == '1':
    print('\t------------------------------------------------\n\tO preço do produto sairá a: R$ {:.2f} reais'.format(produto -( produto * 0.10)))
elif pagamento =='2':
    print('\t------------------------------------------------\n\tO preço do produto sairá a: R$ {:.2f} reais'.format(desc_5))
elif pagamento == '3':
    print('\t------------------------------------------------\n\t------------------------------------------------\n\tVai sair pelo preço normal do valor e você pagará R${:.2f}'.format(produto/2))
elif pagamento == '4':
    print('\t------------------------------------------------\n\tAs parcelas sairão no valor de {:.2f} e o valor total é: R${:.2f} reais '.format((produto * 0.2 + produto) / 3, produto * 0.2 + produto))

if pagamento != '1' and pagamento != '2' and pagamento != '3' and pagamento != '4':
    print('Digite um dos valores acima. Retomando operação.')
