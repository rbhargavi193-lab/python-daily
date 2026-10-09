import random

options = ["rock", "paper", "scissors"]

while True:
    player_score = 0
    computer_score = 0

    for round_num in range(1, 4):
        print("\nRound", round_num)
        player = input("rock, paper or scissors: ").lower()
        computer = random.choice(options)
        print("Computer chose:", computer)

        if player not in options:
            print("Invalid choice, round skipped")
        elif player == computer:
            print("Draw")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    print("\nFinal score - You:", player_score, "Computer:", computer_score)

    if player_score > computer_score:
        print("You win the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("Game is a draw!")

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break