class ChkArmstrong:

	def __init__(self,iValue):
		self.iValue = iValue
		self.iOriginal = iValue

	def Check(self):
		iSum = 0
		iNo = self.iValue
		while(iNo != 0):
			iDigit =  int(iNo % 10)

			iSum = iSum + (iDigit*iDigit*iDigit)

			iNo = iNo / 10

		if(iSum == int(self.iOriginal)):
			return True
		else:
			return False

def main():
	print("Enter the number")
	iNumber = int(input())
	
	obj = ChkArmstrong(iNumber)
	if(obj.Check()):
		print("It is armstrong number...")
	else:
		print("It is not armstrong number...")

if __name__ == "__main__":
	main()