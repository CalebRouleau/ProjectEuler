import math
import sys

#credit for ideas goes to holmezideas.com
#returns True is the input is a prime number
#and false otherwise
def isPrime(num): 
	assert num == int(num)
	num = int(num);
	if(num<=1): 
		return False
	if(num==2): 
		return True
	if(num%2==0): 
		return False
	sqroot = math.sqrt(num); 

	i = 3
	while(i<=sqroot): 
		if(num%i==0): 
			return False
		i+=2
	
	return True


#maxP is the greatest prime that this function
#will generate
def getPrimes(maxP): 
	primes = [];
	allnums = [];
	for num in range(0, maxP+1): 
		allnums.append(1);
		#allnums[num] = 1;

	i = 2;
	while(i<=maxP): 
		if allnums[i] == -1: 
			i += 1;
			continue;

		primes.append(i);
		multis = i*i; 

		while(multis <= maxP): 
			allnums[multis] = -1;
			multis += i

		i += 1;

	return primes;


if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert isPrime(13)
		assert not isPrime(14)

		assert getPrimes(7) == [2, 3, 5, 7]


