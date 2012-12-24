import math
import sys

lengthCount = [0, 9, 100, 1000, 10000, 100000, 1000000]

def getNumDigits(num): 
	return int(math.log10(num))+1;

def digitSearch(digit): 
	lengthRange = 0;
	for length in range(1, 6): 
		newD = digit - length*lengthCount[length]
		if newD < 0: 
			lengthRange = length
			break
		else: 
			digit = newD
	
	#find where digit is in lengthRange
	

def main(): 
	expr = 1; 
	for exp in range(7): 
		digit = int(math.pow(10,exp))
		print digit; 

	


if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert True
		assert getNumDigits(10) == 2
		assert getNumDigits(5) == 1
		assert getNumDigits(2345) == 4
		assert getNumDigits(1) == 1
	else: 
		main()
