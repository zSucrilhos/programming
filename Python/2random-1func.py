def rand_two(min, max):
	from random import choice
	import time
	nmbr = []
	n = 0
	while n <= max:
		for n in range(min, max):
			n += 1
			sysClock = int(time.time())
			#random_nmbr = time*(max-min)*10
		print(sysClock)
	

	#for n in range(min, max):
	#	nmbr.append(min)

	#final_nmbr = choice(nmbr)
	#print(final_nmbr)
	#return final_nmbr
	
rand_two(0, 800)

if __name__ == '__main__':
	rand_two(0,800)



