no_subs=""
sub=""
grade=""
sum=0
ave=0
i=0

no_subs=(eval(input("How many subjects do you have last sem?: ")))

while i != no_subs:
	sub=(input("Name of the subject: "))
	grade=(eval(input("Grade: ")))
	
	sum=sum+grade
	i=i+1
	
ave=sum/no_subs

print("Your average last semester is", round(ave, 2))

print()
print("Average Prediction")

from random import randint
a=randint(97,100)
b=randint(94, 96)
c=randint(90, 93)
d=randint(85, 89)
e=randint(80, 84)
f=randint(75, 79)
g=randint(70, 74)

if 97<=ave<=100:
	print("Your predicted average is ", (a+ave)/2)
	
elif 94<=ave<=96:
	print("Your predicted average is ", (b+ave)/2)

elif 90<=ave<=93:
	print("Your predicted average is ", (c+ave)/2)
	
elif 85<=ave<=89:
	print("Your predicted average is ", (d+ave)/2)
	
elif 80<=ave<=84:
	print("Your predicted average is ", (e+ave)/2)
	
elif 75<=ave<=79:
	print("Your predicted average is ", (f+ave)/2)

elif ave<75:
	print("Your predicted average is ", (g+ave)/2)

