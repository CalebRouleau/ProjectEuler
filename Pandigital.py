import math
import sys
import Truncatable
import DoubleBase

def appendNums(num1, num2): 
	num1 = int(num1); 
	num2 = int(num2); 
	return int(num1*Truncatable.getMagnitude(num2)*10 + num2)

# return True if one of the digits in the number is 
# duplicated and False otherwise
def digitDupe(pan): 
	panSpan = [0,0,0,0,0,0,0,0,0]
	for index in range(int(math.log10(pan))+1): 
		value = DoubleBase.getIndex10(pan, index)
		if(panSpan[value-1] == 1): 
			return True
		else: 
			panSpan[value-1] = 1; 
	return False

def getPandigital(seed): 
	if(digitDupe(seed)): 
		return -1
	pan = appendNums(seed, seed*2)
	if(digitDupe(pan)): 
		return -1
	i = 3
	while(int(math.log10(pan)) < 8): 

		pan = appendNums(pan, seed*i)
		if(digitDupe(pan)): 
			return -1
		i += 1

	if(int(math.log10(pan)) == 8): 
		return pan
	
	return -1
		

def main(): 
	maxPan = -1
	for seed in range(1, 9999): 
		pan = getPandigital(seed)
		if(pan > maxPan): 
			print seed
			maxPan = pan
	print maxPan


if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert True

		assert appendNums(1,4) == 14
		assert appendNums(154,474) == 154474
		assert appendNums(4,474) == 4474
		assert appendNums(447,4) == 4474

		assert getPandigital(9) == 918273645
		assert getPandigital(23423) == -1
		assert getPandigital(98) == -1
	else: 
		main()
