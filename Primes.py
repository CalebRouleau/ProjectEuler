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
