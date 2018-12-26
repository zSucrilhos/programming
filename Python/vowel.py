#-*-coding: utf-8 -*-
def vowel():
	vogal = str(input("Digite uma letra do alfabeto: "))
	if vogal in('a','e','i','o','u'):
		print("A letra é uma vogal!")
		vowel()
	elif vogal in('1','2','3','4','5','6','7','8','9','0'):
		print("Por favor, digite apenas letras.")
		vowel()
	else:
		print("A letra é uma consoante!")
		vowel()

if __name__ == '__main__':
	vowel()
