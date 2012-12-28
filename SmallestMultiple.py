import math
import sys
from Primes import getPrimes


def main(): 
	factors = dict(); 
	for prime in getPrimes(20): 
		factors[prime] = 0; 

	for divisor in range(2, 21): 
		for factor in factors: 
			count = 0
			num = divisor
			while(num%factor == 0): 
				count += 1
				num = num/factor
			if count > factors[factor]: 
				factors[factor] = count
	
	multiple = 1
	for factor in factors: 
		while(factors[factor] != 0): 
			factors[factor] -= 1
			multiple *= factor
	print factors
	print multiple


if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert True
	else: 
		main()
