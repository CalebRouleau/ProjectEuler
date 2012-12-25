import math
import sys
import Primes
import itertools
import Pandigital


def getListNumber(listN): 
	num = listN[0]; 
	for part in range(1,len(listN)): 
		num = Pandigital.appendNums(num, listN[part]); 
	return num


def main(): 
	maxN = 0; 
	nums = [1,2,3,4,5,6,7]
	nums.reverse(); 
	print nums
	for perm in itertools.permutations(nums): 
		#print perm
		num = getListNumber(perm)
		#print num
		if(num > maxN and Primes.isPrime(num)): 
			maxN = num
			print maxN
	print maxN


if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert True
		print Primes.getPrimes(1000000000)[1000]
		
	else: 
		main()
