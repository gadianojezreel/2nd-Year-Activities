from random import randint
a=(randint(1, 99))
b=(randint(1, 99))
c=(randint(1, 99))
d=(randint(1, 99))
e=(randint(1, 99))

a1=(randint(0, 100))
b1=(randint(0, 100))
c1=(randint(0, 100))
d1=(randint(0, 100))
e1=(randint(0, 100))

a2=a+(a1/100)
b2=b+(b1/100)
c2=c+(c1/100)
d2=d+(d1/100)
e2=e+(e1/100)

average=(a2+b2+c2+d2+e2)/5

print("First random decimal number: ", a2)
print("Second random decimal number: ", b2)
print("Third random decimal number: ", c2)
print("Fourth random decimal number: ", d2)
print("Fifth random decimal number: ", e2)
print("")
print("The average of 5 random decimal numbers is ", round(average, 2), ".", sep="")