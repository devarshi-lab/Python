def display(no):
	i = 1;
	while i < no+1:
		print("*",end = " ")
		i += 1;

def main():
	print("Enter a number :",end = " ")
	number = int(input())
	display(number)

if __name__ == "__main__":
	main()
	