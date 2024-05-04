x=(eval(input("How many Fibonacci numbers you want print?: ")))
first = 1
second = 1
print(first)
print(second)
for x in range(x-2):
    third = first + second
    print(third)
    first, second = second, third
    
