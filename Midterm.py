print("Welcome to the Exponential Calculator!")
print("Simply input the base and the exponent to get the result.")
print()

base=""
exponent=""

while True:
	base=(eval(input("Enter the base value (or 0 to exit): ")))
	if base != 0:
		exponent=(eval(input("Enter the exponent value: ")))
		print(base, "to the power of", exponent, "is", base**exponent, end=".")
		print()
		print()
		continue
		
	elif base==0:
		pass
		print()
		print("Thank you for using the Exponential Calculator!")
		print("I hope you had fun! Goodbye!")
		break