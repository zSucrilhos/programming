# -*- coding: utf-8 -*-
i = 0
for i in range(100):
	i += 1
	if i / i == 1 and i / 1 == i:
		print(f'{i} is a prime number!')
	else:
		print(f'{i} is not a prime number!')
		