###############################################################################
# MIT License #
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###############################################################################

# -*- coding: utf-8 -*-
from random import randint, choice
import argparse

# Necessary to generate a psw only with special characters
specchars = ['!','@','#','$','%','&','*','(',')','-','_','=','+']

# Necessary to intialize the variable
psw_length = int(0)

def gen_psw(psw_length, psw_type):
	"""
	Generating the password:
	This uses a random number and then convert it
	into ASCII using the convert_into_ascii() function
	"""
	psw_list = [] # A place to store the passwords :)

	if psw_type == 1:
		for n in range(0, psw_length):
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
		psw_list = [] # Clean the list again
	elif psw_type == 4:
		for n in range(0,psw_length):
			n += 1
			# Using a list to iterate in the special chars because couldn't \n
			# do it with the ASCII table way
			char = choice(specchars)
			almost_formated_psw = psw_list.append(char)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clean the list to store more passwords
	elif psw_type == 5:
		for n in range(0,psw_length):
			n += 1
			# Generate a mixed combination of all the chars
			rand = int(randint(33,126)) 
			rand2 = convert_into_ascii(rand)
			almost_formated_psw = psw_list.append(rand2)
			finally_formated_psw = ''.join(psw_list)
		print(finally_formated_psw)
		psw_list = [] # Clean the list to store even more passwords
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
		description = "psw-generator: A simple python program to generate passwords",
		usage="%(prog)s [options]",
		prefix_chars="-",
	)

	########################
	# Adding the arguments #
	########################

	# Get the number of passwords
	parser.add_argument(
		"-r",
		type=int,
		default=1,
		dest="repeat",
		help="Repeat: Number of passwords to be generated at a time (default=1 password)"
		)

	# Get the password length
	parser.add_argument(
		"-l",
		type=int,
		default=25,
		dest="length",
		help="Length: The lenght of the password to be generated (default=25 chars long)")

	# Get the password type
	parser.add_argument(
		"-t",
		type=int,
		default=5,
		choices=range(1,6),
		dest="type",
		# DON'T TOUCH THE WHITESPACES, PLEASE!
		help="""
Type:
The type of the password to be generated (default= 5).\n
  Possible types are:                                  \n
     1 - UPPERCASE ONLY                                     \n
     2 - lowercase only                                     \n
     3 - 1234567890 only                                    \n
     4 - !@#$%%¨&* only                                      \n
     5 - Mixed 12ab!@                                         \n
"""
)
	# 144: Escaped '%' because it was interfering with \n
	# "self._get_help_string(action) %" in the argparse module

	# Show the program's version
	parser.add_argument(
		"-v",
		dest="version",
		action="store_const",
		const="psw-generator ASCII Version v2.0.3(24012019-11.25)\n\
by Erick César M. GitHub: https://github.com/zSucrilhos",
		help="Version: Show the program's version and exit."
		)

	# Parse the arguments
	arguments = parser.parse_args()

	# Print the program's version
	if arguments.version:
		print(arguments.version)

	# Continue the program if the user don't specify the "-v" argument
	if not arguments.version:
		for i in range(0, arguments.repeat): # Repeat the function X times
			gen_psw(psw_length=arguments.length, psw_type=arguments.type)

