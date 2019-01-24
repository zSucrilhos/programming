# -*- coding: utf-8 -*-
from random import randint, choice
import argparse
import sys

# Necessary to generate a psw only with special characters
specchars = ['!','@','#','$','%','&','*','(',')','-','_','=','+']

# Necessary to intialize the variable
psw_length = int(0)

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
		# Cleaning the list after the storage to be able to store in it again \n
		# later
		psw_list = [] 
	elif psw_type == 2:
		for n in range(0,psw_length):
			n += 1
			# We need some random numbers to convert to ASCII
			rand = int(randint(97,122)) # This time, only lowercase
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
			# Using a list to iterate in the special chars bc couldn't do it \n
			# with ASCII table
			char = choice(specchars)
			almost_formated_psw = psw_list.append(char)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clear the list
	elif psw_type == 5:
		for n in range(0,psw_length):
			n += 1
			# Generate a mixed combination of all the chars
			rand = int(randint(33,126)) 
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
		"-np, --repeat",
		type=int,
		default=1,
		dest="repeat",
		help="How many passwords to be generated at a time (default=1 password)"
		)

	parser.add_argument(
		"-pl, --length",
		type=int,
		default=25,
		dest="length",
		help="The lenght of the password to be generated (default=25 chars long)")

	parser.add_argument(
		"-pt, --type",
		type=int,
		default=5,
		dest="type",
		help="\
		The type of the password to be generated (default= 5 - Mixed).\n\
		Possible types are:\
		1 - UPPERCASE ONLY\
		2 - lowercase only\
		3 - 1234567890 only\
		4 - !@#$%%¨&* only\
		5 - Mixed 12ab!@\
		")

	#parser.add_argument(
	#	"-v, --version",
	#	type=str,
	#	dest="version",
	#	action="store_const",
	#	const="2.0.0",
	#	help="Show the program's version.")

	# Parse the arguments
	arguments = parser.parse_args()

	for i in range(0, arguments.repeat):
		gen_psw(psw_length=arguments.length, psw_type=arguments.type)

	#print(arguments.version)

	#if arguments.version == True:
		print(arguments.version)
