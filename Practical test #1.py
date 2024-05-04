print("\t\tJEZREEL'S FUNKO STORE")
print("\tPAYDAY SALE! UP TO 30% OFF PER FUNKO POP!")
print("")
print("\t\t\t Items")
print("")
print("Code \t Product Description \t Price")
print("")
print("11 \t\t Captain America \t\t P 630")
print("22 \t\t Iron Man \t\t\t\t P 750")
print("33 \t\t Thor \t\t\t\t\t P 700")

print("")

total=0


x=(eval(input("How many orders do you want to purchase?: ")))
for i in range(x):
	a1=(eval(input("Type the code of your choice: ")))
	a2=(eval(input("Type the quantity of your order: ")))
	if a1==11:
		total=total+(630*a2)
		print(a2, "- Captain America \t P", 630*a2)
		print("")
	
	elif a1==22:
		total=total+(750*a2)
		print(a2, "- Iron Man \t P", 750*a2)
		print("")
	
	elif a1==33:
		total=total+(700*a2)
		print(a2, "- Thor \t P", 700*a2)
		print("")

print("")		
print("Total purchase: P ", total)

p=(eval(input("Payment Amount: P ")))

if p>=total:
    print("Your change is P", p-total)
    print("")
    print("Thank you and come again!")
else:
    print("")
    print("Insufficient amount!")
    
    



