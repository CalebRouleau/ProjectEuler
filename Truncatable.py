import math
import sys
import Primes


# if 54, return 10. if 234523 return 100000. etc.
def getMagnitude(num): 
	num = int(num); 
	return int(math.pow(10, int(math.log10(num))))

def truncLeft(num): 
	return num%getMagnitude(num)

def truncRight(num): 
	return int(num/10)


#return True if prime can be truncated to a truncatable
#prime in truncator's direction
def primeTruncatable(num, primesSet, truncator): 
	num = truncator(num)
	while(num != 0):
		if(num not in primesSet): 
			return False
		num = truncator(num)
	return True


def getTruncPrimes(primes): 
	primesSet = set(primes); 
	truncPrimes = [];

	#0 is returned when a single-digit prime
	#is truncated
	primesSet.add(0);

	for prime in primes: 
		if(primeTruncatable(prime, primesSet, truncLeft) and 
				primeTruncatable(prime, primesSet, truncRight)): 
			if(getMagnitude(prime) > 1): 
				truncPrimes.append(prime)

	return truncPrimes

def main(): 
	truncPrimes = getTruncPrimes(Primes.getPrimes(1000000));
	truncSum = 0;
	for p in truncPrimes: 
		truncSum += p

	print truncSum


if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert getMagnitude(234) == 100
		assert getMagnitude(10) == 10
		assert getMagnitude(234534) == 100000

		assert truncLeft(2345) == 345
		assert truncLeft(10) == 0
		assert truncLeft(1) == 0

		assert truncRight(23453) == 2345
		assert truncRight(1) == 0
		
	else: 
		main()
