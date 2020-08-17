def ChkDivisible(no):
	if(no == 0):
		return False
	if(no%5==0):
		return True
	else:
		return False
def main():
	print("Enter the number to check : ")
	number=int(input())
	if ChkDivisible(number):
		print("Divisible by 5")
	else:
		print("Not Divisible by 5")

if __name__ == "__main__":
	main() 