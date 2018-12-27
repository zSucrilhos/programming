# -*- coding: utf-8 -*-
import random
import os
from time import sleep
from string import ascii_uppercase, ascii_lowercase, digits

# Declaring all lists with the standard library
alldata = [ascii_lowercase, ascii_uppercase, digits, specchars]
uppercase = [ascii_uppercase]
lowercase = [ascii_lowercase]
nums = [digits]
specchars = ['!','@','#','$','%','&','*','(',')','-','_','=','+']
psw_list = []
psw_length = int(0)

# Clear the screen according to the OS the user is running
def init():
	if os.name in('nt', 'me', 'ce'):
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")

# Starting the script
def main():
	print("#"*25 + " Password Generator " + "#"*25)
	print()
	print("What is the password's length? ")
	global psw_length
	psw_length = int(input(">> "))
	gen_psw()

# Generating the password
def gen_psw():
	global finally_formated_psw

	print("How do you want your password?")
	print("\n\t1 - UPPERCASE ONLY\n\t2 - lowercase only\n\t3 - 1234567890 only\n\t\
		4 - !@#$%¨&* only\n\t5 - Mixed 12ab!@\n\t")
	psw_chars_type = str(input(">> "))
	if psw_chars_type == "1":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(uppercase)
			almost_formated_psw = psw_list.append(generated_psw)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
	elif psw_chars_type == "2":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(lowercase)
			almost_formated_psw = psw_list.append(generated_psw)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
	elif psw_chars_type == "3":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(nums)
			almost_formated_psw = psw_list.append(generated_psw)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
	elif psw_chars_type == "4":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(specchars)
			almost_formated_psw = psw_list.append(generated_psw)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
	elif psw_chars_type == "5":
		print("Here is your password, store it with care: ")
		for n in range(0,psw_length):
			n += 1
			generated_psw = random.choice(alldata)
			almost_formated_psw = psw_list.append(generated_psw)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
	else:
		print("Please, select one of the options listed.")
		gen_psw()
	write_psw_hdd()

# Write the password to an file on the disk
def write_psw_hdd():
	print()
	print("Save the password to a txt (plain text) file? (Y/N)\n\t")
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
		write_psw_hdd()

# Ask if the user wants to generate another password calling main()
def gen_psw_again():
	print()
	print("Generate another password? (Y/N)")
	loop = str(input(">> ".lower()))
	if loop == "y":
		main()
	elif loop == "n":
		print()
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
