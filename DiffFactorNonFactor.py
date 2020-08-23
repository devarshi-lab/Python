'''
Accept number from user and return difference between summation of non
factors and summation of factors.
In this question you have to write the logic which should not be dependent on
other function.
Input : 12
Output : 34 ((5 + 7 + 8 + 9 + 10 + 11) - (1 + 2 + 3 + 4 + 6))
Input : 9
Output : 28 ((2 + 4 + 5 + 6 + 7 + 8) - (1 + 3)) 
'''

def DiffFactorNonFactor(value):
	iFactor = 0
	iNonfactor = 0
	for i in range(1,value):
		if(value % i == 0):
			iFactor += i
		else:
			iNonfactor += i;
	return (iNonfactor-iFactor)


def main():
	print("Enter the number",end = " ")
	number = int(input())
	ans = DiffFactorNonFactor(number)
	print("Difference bertween the addition of factors and non-factors is : ",ans)

if __name__ == "__main__":
	main()


