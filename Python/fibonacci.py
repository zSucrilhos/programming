from time import sleep

def main():
	try:
		rng = int(input("What is the range? "))
		fibonacci(rng)
	except ValueError:
		print("You must enter an interger")
		main()
		
def fibonacci(rng):
	for c in range(0, rng):
		c = c-1
		c += 1
		fb_nmbr = 
		print(c)
		sleep(0.7)

if __name__ == "__main__":
	main()