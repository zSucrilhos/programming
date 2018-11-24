# -*- coding: utf-8 -*-
import random
import os

alldata = [
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
'!','@','#','$','%','&','*',\
'1','2','3','4','5','6','7','8','9','0'
]

prompt1_psw_size = int(0)

if os.name in('nt', 'me', 'ce'):
	os.system("cls")
elif os.name == "posix":
	os.system("clear")

print("#"*25 + " Password Generator " + "#"*25)
print()
prompt1_psw_size = str(input("What is the password's size? \n\n\t1 - 08 Characters\n\t2 - 16 Characters\n\t\
3 - 24 Characters\n\t4 - 32 Characters\n\t\n>> "))

if prompt1_psw_size == "1":
	print("Here is your password, store it with care: ")
	for n in range(0,8):
		n += 1
		print(random.choice(alldata), end="")
	print()
elif prompt1_psw_size == "2":
	print("Here is your password, store it with care: ")
	for n in range(0,16):
		n += 1
		print(random.choice(alldata), end="")
	print()
elif prompt1_psw_size == "3":
	print("Here is your password, store it with care: ")
	for n in range(0,24):
		n += 1
		print(random.choice(alldata), end="")
	print()
elif prompt1_psw_size == "4":
	print("Here is your password, store it with care: ")
	for n in range(0,32):
		n += 1
		print(random.choice(alldata), end="")
	print()

