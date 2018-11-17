numero = int(input("Digite um número: "))
for c in range(0,11):
	print("{:2} x {:2} = {:2}" .format(numero, c, c*numero))
	c += 1
