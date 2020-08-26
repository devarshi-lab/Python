'''
Accept range from user and return addition of prime numbers in between that
range.
Input : 10 20
Output : 60 (11 + 13 + 17 + 19) 
'''

def PrimeAddition(iBeg,iEnd):
	iAns = 1
	iSum = 0
	pSum = 0
	for j in range(iBeg,iEnd+1):
		for i in range(2,j+1):
			if(j % i == 0):
				pSum += i
			if(pSum == j):
				iSum += j
		pSum = 0
	return iSum			

def main():
	print("Enter the range : ")
	iStart = int(input())
	iStop = int(input())
	print("Addition of prime numbers between",iStart,"and",iStop,"is :",PrimeAddition(iStart,iStop))

if __name__ == "__main__":
	main()
