
print("=====ROCK-PAPER-SCISSORS GAME=====")

import random

options = ( "rock","paper","scissors")
is_running = True
player_score=0
computer_score=0


while is_running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input('Enter a choice (rock,paper,scissors): ').lower()


    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player==computer:
        print("It's a tie!")

    elif player =="rock" and computer =="scissors":
        print("You win!")
        player_score+=1
    elif player=="paper" and computer=="rock":
        print("You win!")
        player_score+=1
    elif player=="scissors" and computer=="paper":
        print("You win!")
        player_score+=1
    else:
        print("Computer wins!")
        computer_score+=1

    print(f"Player score: {player_score}  || Computer score: {computer_score}")

    play_again=input("Play again? (y/n): ").lower()
    if not play_again=="y":
        is_running=False

print()
print("------FINAL SCORE------")
print(f"Player score: {player_score}  || Computer score: {computer_score}")
print("-----------------------")
print()
print("Thanks for playing!!")
print()








