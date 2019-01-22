# -*- coding: utf-8 -*-
from random import randint, choice
from os import system, name
from time import sleep
import argparse

# Necessary to generate a psw with only special characters
specchars = ['!','@','#','$','%','&','*','(',')','-','_','=','+']

# Necessary to intialize the variable
psw_length = int(0)

#def main():
#	gen_psw(psw_length, psw_type)

def gen_psw(psw_length, psw_type):
	"""
	Generating the password:
	This uses an random number and then convert it
	into ASCII using the convert_into_ascii() function
	"""
	psw_list = [] # A place to store the passwords :)

	if psw_type == 1: 
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(65,90)) # We will use only UPPERCASE chars here
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Cleaning the list after the storage to be able to store in it again later
	elif psw_type == 2:
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(97,122)) # This time, only lowercase ones
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clean the list
	elif psw_type == 3:
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(48,57)) # Here we use only numbers
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = []
	elif psw_type == 4:
		for n in range(0,psw_length):
			n += 1
			# Using a list to iterate in the special chars bc couldn't do it with ASCII table
			char = choice(specchars)
			almost_formated_psw = psw_list.append(char)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clear the list
	elif psw_type == 5:
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(33,126)) # Generate a mixed combination of all the chars
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clean the list
	else:
		print("You must specify at least one argument")
		exit(1)
	
def convert_into_ascii(dec):
	""" Convert the given input into ASCII """
	char = str(chr(dec))
	return char

if __name__ == '__main__':
	# Initialize the parser 
	parser = argparse.ArgumentParser(
		description = "A simple program to generate passwords"
	)

	# Adding the arguments
	parser.add_argument(
		"pl, --psw_length",
		type=int,
		help="The lenght of the password to be generated")

	parser.add_argument(
		"-pt, --psw_type",
		type=int,
		default=5,
		help="\
The type of the password to be generated.\n\
Possible types are:\n\t\
1 - UPPERCASE ONLY\n\t\
2 - lowercase only\n\t\
3 - 1234567890 only\n\t\
4 - !@#$%¨&* only\n\t\
5 - Mixed 12ab!@\n\t"
)

	# Parse the arguments
	arguments = parser.parse_args()

	# Do something for now i don't know what
	gen_psw(psw_length, psw_type)
	#if args.psw_length and args.psw_type:
	#	gen_psw(psw_length, psw_type)
	#elif args.help:
