import math
import sys


def main(): 
	pMax = 0
	maxCount = 0
	for p in range(1, 1001): 
		tCount = 0 #triangle count
		for a in range(1, int(p/2)): 
			if((p*p - 2*p*a)%(2*(p-a)) == 0): 
				tCount += 1; 
		if(tCount > maxCount): 
			maxCount = tCount
			pMax = p
	print maxCount
	print pMax


if __name__ == "__main__": 
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert True
	else: 
		main()
