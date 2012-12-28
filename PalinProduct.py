import math
import sys
from DoubleBase import isPalindrome, getIndex10


def main(): 
	maxP = 0;
	for n1 in reversed(range(100, 1000)):
		for n2 in reversed(range(100, 1000)): 
			guess = n1*n2
			if(isPalindrome(guess, 15, getIndex10)): 
				if guess > maxP:
					maxP = guess
	print maxP




if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert True
	else: 
		main()
