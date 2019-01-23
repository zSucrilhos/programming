# -*- coding: utf-8 -*-
from random import randint, choice
import argparse
import sys

# Necessary to generate a psw only with special characters
specchars = ['!','@','#','$','%','&','*','(',')','-','_','=','+']
version = "2.0.2"
build = "23012019"
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
	return 0
		
def convert_into_ascii(dec):
	""" Convert the given input into ASCII """
	char = str(chr(dec))
	return char

if __name__ == '__main__':
	# Initialize the parser 
	parser = argparse.ArgumentParser(
		description = "A simple program to generate passwords"
	)

	########################
	# Adding the arguments #
	########################

	# Get the number of passwords
	parser.add_argument(
		"-np, --repeat",
		type=int,
		default=1,
		dest="repeat",
		help="Number of passwords to be generated at a time (default=1 password)"
		)

	# Get the password length
	parser.add_argument(
		"-pl, --length",
		type=int,
		default=25,
		dest="length",
		help="The lenght of the password to be generated (default=25 chars long)")

	# Show the program's version
	parser.add_argument(
		"-v, --version",
		dest="version",
		action="store_const",
		const="psw-generator ASCII Version v{version}({build}) - by Erick César M.\n\
GitHub: https://github.com/zSucrilhos",
		help="Show the program's version.")

	# Get the password type
	parser.add_argument(
		"-pt, --type",
		type=int,
		default=5,
		dest="type",
		help="\
The type of the password to be generated (default= 5 - Mixed).\n\
Possible types are:\n\
\t1 - UPPERCASE ONLY\n\
\t2 - lowercase only\n\
\t3 - 1234567890 only\n\
\t4 - !@#$%%¨&* only\n\
\t5 - Mixed 12ab!@\
		")
	# 114: Escaped '%' because it was interfering with
	# "self._get_help_string(action) %" in the argparse module

	# Parse the arguments
	arguments = parser.parse_args()

	# Print the program's version
	if arguments.version:
		print(arguments.version)

	# Continue the program if the user don't specify the "-v" argument
	if not arguments.version:
		for i in range(0, arguments.repeat): # Repeat the function X times
			gen_psw(psw_length=arguments.length, psw_type=arguments.type)
