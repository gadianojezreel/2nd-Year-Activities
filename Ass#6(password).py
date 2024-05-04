password=12345
enter_pass=""

i = 5

while i!=0:
    enter_pass=(eval(input("Enter your password: ")))
    i=i-1
    if enter_pass!=password and i>=2:
        print("Wrong password! Try Again!")
        print("You only have", i, "attempts left.")
        continue
    
    elif enter_pass!=password and i==1:
        print("Wrong password! Try Again!")
        print("You only have", i, "attempt left.")
        continue
    
    elif enter_pass!=password and i==0:
        print("You are now kick off the system.")
    
    elif enter_pass==password:
        print("You are now logged in to the system.")
        break
    

