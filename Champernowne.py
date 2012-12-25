import math
import sys
import DoubleBase
import Truncatable

lengthCount = [0, 9, 100, 1000, 10000, 100000, 1000000]

def getNumDigits(num): 
	return int(math.log10(num))+1;

def getDigits(digit): 
	inputDigit = digit

	digit -= 1

	count = 1
	magnitude = 0
	
	finished = False
	if(not finished): 
		if(digit - 9 > 0): 
			digit -= 9
			count += 9
		else: 
			finished = True
			magnitude = 1

	if(not finished): 
		if(digit - 90*2 > 0): 
			digit -= 90*2
			count += 90
		else: 
			finished = True
			magnitude = 2

	if(not finished): 
		if(digit - 900*3 > 0): 
			digit -= 900*3
			count += 900
		else: 
			finished = True
			magnitude = 3

	if(not finished): 
		if(digit - 9000*4 > 0): 
			digit -= 9000*4
			count += 9000
		else: 
			finished = True
			magnitude = 4

	if(not finished): 
		if(digit - 90000*5 > 0): 
			digit -= 90000*5
			count += 90000
		else: 
			finished = True
			magnitude = 5

	if(not finished): 
		if(digit - 900000*6 > 0): 
			digit -= 900000*6
			count += 900000
		else: 
			finished = True
			magnitude = 6

	assert finished
	count += int(digit/magnitude)
	subDigit = digit%magnitude
	print "input digit is", inputDigit
	print "digit is",digit
	print "magnitude is",magnitude
	print "count is",count
	print "subDigit is", subDigit
	countOrder = getNumDigits(count)
	print "countOrder is", countOrder
	returnValue = DoubleBase.getIndex10(count, countOrder -subDigit-1)
	print "return value is",returnValue
	return returnValue
		

def main(): 
	expr = 1; 
	for exp in range(7): 
		digit = int(math.pow(10,exp))
		expr *= getDigits(digit)
	print expr


if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert True
		assert getNumDigits(10) == 2
		assert getNumDigits(5) == 1
		assert getNumDigits(2345) == 4
		assert getNumDigits(1) == 1


		assert getDigits(4) == 4
		assert getDigits(14) == 1
		assert getDigits(15) == 2
		assert getDigits(16) == 1
		assert getDigits(17) == 3
		assert getDigits(18) == 1
		assert getDigits(19) == 4


	else: 
		main()
