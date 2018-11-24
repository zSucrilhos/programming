# -*- coding: utf-8 -*-
import random
import os
from time import sleep

alldata = [
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
'!','@','#','$','%','&','*',\
'1','2','3','4','5','6','7','8','9','0'
]

psw_length = int(0)

def init():
	if os.name in('nt', 'me', 'ce'):
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")

def main():
	print("#"*25 + " Password Generator " + "#"*25)
	print()
	print("What is the password's length? ")
	global psw_length
	psw_length = int(input(">> "))

	gen_psw()

def gen_psw():
	print("Here is your password, store it with care: ")
	for n in range(0,psw_length):
		n += 1
		print(random.choice(alldata), end="")
	print()

	gen_psw_again()

def write_psw_hdd(filename):
	print("")
	print("Save the password to a txt (plain text) file? (Y/N)\n\t")
	write_prompt = str(input(">> ".lower()))
	if write_prompt == "y":
		print("Save file as: \n\t")
		write_filename = str(input("Filename >> "))
		open(filename, 'w', encoding='utf-8')
		print("File saved sucessfully in the script's directory.\n")
		print("")
		gen_psw_again()
	elif write_prompt == "n":
		init()
		gen_psw_again()
	elif write_prompt not in('y', 'n'):
		print("Please, enter only 'Y' or 'N'.")
		write_psw_hdd()

def gen_psw_again():
	print("")
	print("Generate another password? (Y/N)")
	loop = str(input(">> ".lower()))

	if loop == "y":
		init()
		main()
	elif loop == "n":
		print("")
		print("Bye!")
		sleep(0.3)
		init()
		exit(0)
	elif loop not in('y', 'n'):
		print("Please, enter only 'Y' or 'N'.")

		gen_psw_again()


if __name__ == '__main__':
	init()
	main()
