#Determine the value of 2^n and ask the user
#how many last digits of 2^n to display.
print("2^n = ?")
n=eval(input("Enter power or the value of the exponent: "))
l=eval(input("How many last digits of 2^n you want to know?: "))
p=2**n

print("")
print("2 raised to the power of ", n, " is equal to ", p, ".", sep="")
print("Therefore, the last ", l, " digit(s) of 2^", n, sep="", end="")

print(" is ", (p%(10**l)), ".", sep="")
