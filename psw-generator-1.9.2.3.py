# -*- coding: utf-8 -*-
import random
import os
from time import sleep
from string import ascii_uppercase, ascii_lowercase, digits

# Declaring all lists with the standard library
specchars = ['!','@','#','$','%','&','*','(',')','-','_','=','+']
uppercase = list(ascii_uppercase)
lowercase = list(ascii_lowercase)
nums = list(digits)

alldata = lowercase + uppercase + nums + specchars

# Necessary to intialize the variable
psw_length = int(0)

def init():
    """ Clear the screen according to the OS the user is running"""
    if os.name in('nt', 'me', 'ce'):
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print("#"*25 + " Password Generator " + "#"*25)

def main():
        """ Initial function"""
        print("\nWhat is the password's length? ")
        try:
            psw_length = int(input(">> "))
            gen_psw(psw_length)
        except ValueError:
            print("You must enter an integer\n")
            main()

def gen_psw(psw_length):
    """ Generating the password
    This uses the random choice() method and a for loop to iterate into the lists"""
    psw_list = []

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
        psw_list = []
        write_psw_hdd(finally_formated_psw)
    elif psw_chars_type == "2":
        print("Here is your password, store it with care: ")
        for n in range(0,psw_length):
            n += 1
            generated_psw = random.choice(lowercase)
            almost_formated_psw = psw_list.append(generated_psw)
            finally_formated_psw = ''.join(psw_list)
        print(finally_formated_psw)
        psw_list = []
        write_psw_hdd(finally_formated_psw)
    elif psw_chars_type == "3":
        print("Here is your password, store it with care: ")
        for n in range(0,psw_length):
            n += 1
            generated_psw = random.choice(nums)
            almost_formated_psw = psw_list.append(generated_psw)
            finally_formated_psw = ''.join(psw_list)
        print(finally_formated_psw)
        psw_list = []
        write_psw_hdd(finally_formated_psw)
    elif psw_chars_type == "4":
        print("Here is your password, store it with care: ")
        for n in range(0,psw_length):
            n += 1
            generated_psw = random.choice(specchars)
            almost_formated_psw = psw_list.append(generated_psw)
            finally_formated_psw = ''.join(psw_list)
        print(finally_formated_psw)
        psw_list = []
        write_psw_hdd(finally_formated_psw)
    elif psw_chars_type == "5":
        print("Here is your password, store it with care: ")
        for n in range(0,psw_length):
            n += 1
            generated_psw = random.choice(alldata)
            almost_formated_psw = psw_list.append(generated_psw)
            finally_formated_psw = ''.join(psw_list)
        print(finally_formated_psw)
        psw_list = []
        write_psw_hdd(finally_formated_psw)
    else:
        print("Please, select one of the options listed.")
        gen_psw(psw_length)
        write_psw_hdd(finally_formated_psw)

def write_psw_hdd(finally_formated_psw):
    """ Ask if the user wants to generate another password calling main()
    and write the file to disk, if wanted by the user.
    this uses the write() method """
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
