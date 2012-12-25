import math
import sys


def main(): 
	sumN = 0

	num = 3
	while(True): 
		if(num <1000): 
			if(num%5 == 0): 
				pass
			else:
				sumN += num
		else: 
			break
		num += 3

	num =5
	while(True): 
		if(num <1000): 
			sumN += num
		else: 
			break
		num += 5

	print sumN



if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert True
	else: 
		main()
