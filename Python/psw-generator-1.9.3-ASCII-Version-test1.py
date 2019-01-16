# -*- coding: utf-8 -*-
from random import randint, choice
from os import system, name
from time import sleep

# Necessary to intialize the variable
psw_length = int(0)

# pass as arguments to use by pipe instead of an interation with the user
def init():
	""" Clear the screen according to the OS the user is running"""
	if name in('nt', 'me', 'ce'):
		system("cls")
	elif name == "posix":
		system("clear")
	print("#"*25 + " Password Generator " + "#"*25)

def main():
	""" Initial function"""
	print("\nWhat is the password's length? ") # We will need this later
	try:
		psw_length = int(input(">> "))
		gen_psw(psw_length)
	except ValueError:
		print("You must enter an integer\n")
		main()

def gen_psw(psw_length):
	""" Generating the password
	This uses an random number and then convert it into ASCII """
	psw_list = [] # A place to store the passwords :)

	print("How do you want your password?")
	print("\n\t1 - UPPERCASE ONLY\n\t2 - lowercase only\n\t3 - 1234567890 only\n\t\
4 - !@#$%¨&* only\n\t5 - Mixed 12ab!@\n\t")
	psw_chars_type = str(input(">> "))
	if psw_chars_type == "1": 
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(65,90)) # We will use only UPPERCASE chars here
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Cleaning the list after the storage to be able to store in it again later
	elif psw_chars_type == "2":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(97,122)) # This time, only lowercase ones
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clean the list
	elif psw_chars_type == "3":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(48,57)) # Here we use only numbers
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = []
	elif psw_chars_type == "4":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand0 = randint(21,47) # Need to fix that
			rand1 = randint(91,126)
			print(f'rand0 = {rand0}')
			print(f'rand1 = {rand1}')
			rand2 = convert_into_ascii(rand0, rand1)
			print('Passou pela função convert_into_ascii()')
			print(f'rand0 = {rand0}')
			print(f'rand1 = {rand1}')
			almost_formated_psw = psw_list.extend([rand0, rand1])
			print('Passou pelo extend da lista')
			print(f'rand0 = {rand0}')
			print(f'rand1 = {rand1}')
			print(psw_list)
			#finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clear the list
	elif psw_chars_type == "5":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(33,126)) # Generating a mixed combination of all the chars
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clean the list
	else:
		print("Please, select one of the options listed.")
		gen_psw(psw_length)
	write_psw_hdd(finally_formated_psw)

def convert_into_ascii(dec, dec1=0):
	""" Convert the given input into ASCII """
	if dec1:
		char = str(chr(dec))
		char1 = str(chr(dec1))
		char2 = str(char + char1)
		print(f'char2 da função convert_into_ascii() = {char2}')
		return str(char2)
	else:
		char = str(chr(dec))
		return str(char)

def write_psw_hdd(finally_formated_psw):
	""" Ask if the user wants to generate another password calling main()
	and write the file to disk, if wanted by the user.
	This uses the write() method """
	print("\nSave the password to a txt (plain text) file? (Y/N)\n\t")
	write_prompt = str(input(">> ".lower()))
	if write_prompt == "y":
		print("Save file as:\t")
		write_filename = str(input("Filename >> "))
		filehandle = open(write_filename + '.txt', 'a', encoding='utf-8')
		filehandle.writelines(finally_formated_psw)
		filehandle.close()
		print("File saved sucessfully in the script's directory.\n")
		gen_psw_again()
	elif write_prompt == "n":
		init()
		gen_psw_again()
	elif write_prompt not in('y', 'n'):
		print("Please, enter only 'Y' or 'N'.")
		write_psw_hdd(finally_formated_psw)

def gen_psw_again():
	""" Ask if the user wants to generate another password calling main()"""
	print("\nGenerate another password? (Y/N)")
	loop = str(input(">> ".lower()))
	if loop == "y":
		main()
	elif loop == "n":
		print("\nBye!")
		sleep(0.3)
		init()
		exit(0)
	elif loop not in('y', 'n'):
		print("Please, enter only 'Y' or 'N'.")
		gen_psw_again()

if __name__ == '__main__':
	init()
	main()
