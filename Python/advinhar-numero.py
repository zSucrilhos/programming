from random import randint
numero = randint(0,10)
temp = 1
print("Tente advinhar o número de 0 a 10.")
usr_num = int(input("\t\nDigite um número de 0 a 10: "))
while usr_num != numero:
	usr_num = int(input("Você erroou! Tente novamente: "))
	temp += 1
else:
	print("Parabéns, você acertou!! O número em que eu estava pensando era {} e você levou {} tentativas para conseguir.".format(numero, temp))