import sys

powersOf10 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
firstDigit10 = 7; 

firstDigit2 = 0; 
oneMillion = 1000000
million = oneMillion
while(million != 0): 
	million >>= 1
	firstDigit2 += 1

def main(): 
	print "in main"; 

	palSum = 0

	num = 1
	while(num < oneMillion): 
		if(isPalin2and10(num)): 
			print num
			palSum += num
		num += 2

	print "answer", palSum


def isPalin2and10(num): 
	return (isPalindrome(num=num, firstDigit=firstDigit2, indexer=getIndex2) and
		isPalindrome(num=num, firstDigit=firstDigit10, indexer=getIndex10))


def getIndex10(num, index): 
	num = int(num/powersOf10[index]); 
	return num % 10; 

def isPalindrome(num, firstDigit, indexer): 
	while(indexer(num, firstDigit) == 0): 
		firstDigit -= 1
	
	index = 0; 
	while(firstDigit-index > index): 
		if(indexer(num, firstDigit-index) != indexer(num, index)): 
			return False;
		index += 1; 

	return True


def getIndex2(num, index): 
	num >>= index;
	return num%2; 

def printBinary(num): 
	string = ""; 
	index = 10; 
	while(index >= 0): 
		string += str(getIndex2(num, index)); 
		index -= 1
	print num, string


if __name__ == "__main__":
	if(len(sys.argv) > 1 and sys.argv[1] == "test"): 
		assert getIndex2(num=1, index=3) == 0; 
		assert getIndex2(num=1, index=0) == 1; 
		assert getIndex2(num=3, index=0) == 1; 
		assert getIndex2(num=3, index=1) == 1; 
		assert getIndex2(num=2, index=0) == 0; 

		assert isPalindrome(num=585, firstDigit=firstDigit2, 
				indexer=getIndex2); 
		assert isPalindrome(num=3, firstDigit=firstDigit2, 
				indexer=getIndex2);
		assert not isPalindrome(num=4, firstDigit=firstDigit2, 
				indexer=getIndex2);
		assert isPalindrome(num=5, firstDigit=firstDigit2, 
				indexer=getIndex2);
		assert not isPalindrome(num=11, firstDigit=firstDigit2, 
				indexer=getIndex2); 
		assert not isPalindrome(num=8586, firstDigit=firstDigit2, 
				indexer=getIndex2); 

		assert getIndex10(65, 0) == 5
		assert getIndex10(65, 1) == 6
		assert getIndex10(546965, 4) == 4

		assert isPalindrome(num=585, firstDigit=firstDigit10, 
				indexer=getIndex10); 
		assert not isPalindrome(num=85, firstDigit=firstDigit10, 
				indexer=getIndex10); 
	else:
		main(); 

