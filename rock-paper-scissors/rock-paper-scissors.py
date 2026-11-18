import random
choices = ["rock", "paper", "scissors"]
print("Welcome to Rock Paper Scissors!")
print("1. Play with Computer")
print("2. Play with Another Player")
mode = input("Choose game mode (1 or 2): ")
rounds = int(input("How many rounds do you want to play? "))
player1_score = 0
player2_score = 0
for round_number in range(1, rounds + 1):
    print("Round", round_number)
    player1 = input("Player 1, choose rock, paper, or scissors: ").lower()
    if player1 not in choices:
        print("Invalid choice! Try again.")
        continue
    if mode == "1":
        player2 = random.choice(choices)
        print("Computer chose:", player2)
    elif mode == "2":
        player2 = input("Player 2, choose rock, paper, or scissors: ").lower()
        if player2 not in choices:
            print("Invalid choice! Try again.")
            continue
    else:
        print("Invalid game mode!")
        break
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        print("Player 1 wins this round!")
        player1_score += 1
    else:
        print("Player 2 wins this round!")
        player2_score += 1
print("\n========== FINAL SCORE ==========")
print("Player 1:", player1_score)
print("Player 2:", player2_score)
if player1_score > player2_score:
    print("Player 1 is the winner!")
elif player2_score > player1_score:
    if mode == "1":
        print("Computer is the winner!")
    else:
        print("Player 2 is the winner!")
else:
    print("The game is a tie!")
print("Thanks for playing!")