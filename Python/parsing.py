import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
parser.add_argument("psw_length", help="Specify the password's lenght", type=int)
args = parser.parse_args()



print(args.psw_length)