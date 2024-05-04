from random import randint
x=randint(1, 20)

print("GUESSING GAME!")
print("Guess the random number from 1 to 20.")
print("You only have 3 chances to guess the number.")
print("The game will stop after you guessed the number correctly or after 3 failed guesses.")


for i in range(3):
    y=(eval(input("Type your guess here: ")))
    if x==y:
        print("Congratulations! You guessed the number!")
        break
    elif x!=y and i<=1:
        print("Oops, Try Again!")
    
    elif x!=y and i==2:
        print("Game Over!") 
        print("The random number is ", x, ".", sep="")
