from random import choice

game = ["ROCK", "PAPER", "SCISSORS"]

score=0
computer_player=choice(game)
print("Rock, Paper, and Scissors")


x=int(input("How many times do you want to play?: "))

for i in range(x):

    player_input= input("Type your choice between ROCK, PAPER, or SCISSORS (use capital letters only): ")
    print("Computer Answer: ", computer_player)

    if computer_player=="ROCK" and player_input=="ROCK":
        print("It's a draw")
    
    elif computer_player=="ROCK" and player_input=="PAPER":
        score=score+1
        print("You won!")
    
    elif computer_player=="ROCK" and player_input=="SCISSORS":
        print("The computer won!")
    
    elif computer_player=="PAPER" and player_input=="PAPER":
        print("It's a draw")
    
    elif computer_player=="PAPER" and player_input=="ROCK":
        print("The computer won!")
    
    elif computer_player=="PAPER" and player_input=="SCISSORS":
        score=score+1
        print("You won!")
    
    elif computer_player=="SCISSORS" and player_input=="SCISSORS":
        print("It's a draw")
    
    elif computer_player=="SCISSORS" and player_input=="ROCK":
        score=score+1
        print("You won!")
    
    elif computer_player=="SCISSORS" and player_input=="PAPER":
        print("The computer won!")
        
print("Your score: ", score, "/", x)
    

