from random import randint
def init():
	length_psw = int(input("How many chars? "))
	gen_psw(length_psw)

def gen_psw(length_psw):
	for n in range(0,length_psw):
		nmbr = randint(33,126)
		print(nmbr, end=" ")	
		convert_into_ascii(nmbr)
		

def convert_into_ascii(dec):
	char = str(chr(dec))
	return char


if __name__ == '__main__':
	init()