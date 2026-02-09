# Rock, Paper, Scissors game

import random

MOVES = ("rock", "paper", "scissors")
human_move = ""
computer_move = ""


while True:
    print("\nLet's play Rock, Paper, Scissors!\n")

    # computer's move by random
    computer_move = random.choice(MOVES)

    # player's move
    while human_move not in MOVES:
        print("Choose your move: rock, paper, or scissors..")
        human_move = input("\nEnter your choice: ").lower()

    print("\nYou chose: ", human_move, "\nAnd I chose: ", computer_move)

    # check for a tie and check for a winner
    if human_move == computer_move:
        print("\n\nIt's a tie!")
    elif human_move == "rock" and computer_move == "scissors":
        print("\nYou win this round! Congratulations!\n")
    elif human_move == "scissors" and computer_move == "paper":
        print("\nYou win this round! Congratulations!\n")
    elif human_move == "paper" and computer_move == "rock":
        print("\nYou win this round! Congratulations!\n")
    else:
        print("\nComputer wins this round!\n")


    human_move = ""
    answer = input("Do you want play again? (yes/no): ").lower()
    if answer == "no":
        print("\nThanks for playing! Bye!")
        input("\nPress Enter to exit")
        break