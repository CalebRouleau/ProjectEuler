import math
import sys

def yieldFib(maxF):
	first = 1
	yield 1
	second = 2
	yield 2

	while(True): 
		newF = first + second
		first = second
		second = newF
		if(newF < maxF): 
			yield newF
		else: 
			break


def main(): 
	sumEven = 0
	for fib in yieldFib(4000000): 
		if fib%2 == 0: 
			sumEven += fib
	print sumEven



if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		fiblist = list(yieldFib(9));
		assert fiblist[3] == 5
	else: 
		main()
