# -*- coding: utf-8 -*-
usr_number = int(input("Enter a number to calculate: "))
if usr_number > 1:
	for n in range(2, usr_number):
		if (usr_number % n == 0):
			print(f'{n} is not a prime number')
		else:
			print(f'{n} is a prime number')
	

