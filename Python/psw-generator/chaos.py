from random import randint
import math
from time import sleep

whi = True
while whi == True:
	n1 = float(randint(0,99))
	n2 = float(randint(0,99))
	print(f'{math.pi*n1**n2}')
	sleep(0.5)
