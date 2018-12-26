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

uppercase = [
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
]

lowercase = [
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
]

nums = [
'1','2','3','4','5','6','7','8','9','0'
]

specchars = [
'!','@','#','$','%','&','*',\
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
	print("How do you want your password?")
	print("\n\t1 - UPPERCASE ONLY\n\t2 - lowercase only\n\t3 - 1234567890 only\n\t4 - !@#$%¨&* only\n\t5 - Mixed 12ab!@\n\t")
	psw_chars_type = str(input(">> "))
	if psw_chars_type == "1":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			global generated_psw
			global generated_psw_line
			generated_psw = random.choice(uppercase)
			generated_psw_line = generated_psw.split()
			print(generated_psw, end="")
		print()
	elif psw_chars_type == "2":
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(lowercase)
			generated_psw_line = generated_psw.split()
			print(generated_psw, end="")
		print()
	elif psw_chars_type == "3":
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(nums)
			generated_psw_line = generated_psw.split()
			print(generated_psw, end="")
		print()
	elif psw_chars_type == "4":
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(specchars)
			generated_psw_line = generated_psw.split()
			print(generated_psw, end="")
		print()
	elif psw_chars_type == "5":
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(alldata)
			generated_psw_line = generated_psw.split()
			# TEST TO SEE IF THE VARIABLE CAN BECOME ONE SINGLE STRING
			psw_to_write = generated_psw, end=""
			print(generated_psw, end="")
			print(f'psw_to_write = {psw_to_write}')
			print(f'generated_psw = {generated_psw}')
			print(f'generated_psw_line = {generated_psw_line}')

		print()
	else:
		print("Please, select one of the options listed.")
		gen_psw()
	write_psw_hdd()

def write_psw_hdd():
	print("")
	print("Save the password to a txt (plain text) file? (Y/N)\n\t")
	write_prompt = str(input(">> ".lower()))
	if write_prompt == "y":
		print("Save file as:\t")
		write_filename = str(input("Filename >> "))
		filehandle = open(write_filename + '.txt', 'a', encoding='utf-8')
		filehandle.writelines(generated_psw)
		filehandle.close()
		print("File saved sucessfully in the script's directory.\n")
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
