import math

#credit for ideas goes to holmezideas.com
def isPrime(num): 
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



def getPrimes(maxP): 
	primes = [];
	allnums = [];
	for num in range(0, maxP): 
		allnums.append(1);
		#allnums[num] = 1;

	i = 2;
	while(i<maxP): 
		if allnums[i] == -1: 
			i += 1;
			continue;

		primes.append(i);
		multis = i*i; 

		while(multis < maxP): 
			allnums[multis] = -1;
			multis += i

		i += 1;

	return primes;
