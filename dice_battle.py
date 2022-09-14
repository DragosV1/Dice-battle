import random
import time


print("Welcome to Dice Battle!")
print("This game is all about luck!\n")

player_name = input("Please enter a name: ")

print("Throwing...")
time.sleep(1.5)

def start_battle():
    dice = [1, 2, 3, 4, 5, 6]

    computer_throw = random.choice(dice)
    player_throw = random.choice(dice)

    while True:
        if computer_throw == player_throw:
            print(f"Computer throw: {computer_throw}  {player_name} throw: {player_throw}")
            print("Draw!")
            print("Throwing again...")
            computer_throw = random.choice(dice)
            player_throw = random.choice(dice)
            time.sleep(1.5)
            continue
        if computer_throw < player_throw:
            print(f"Computer throw: {computer_throw}  {player_name} throw: {player_throw}")
            print(f"{player_name} you won!")
            break
        if computer_throw > player_throw:
            print(f"Computer throw: {computer_throw} {player_name} throw: {player_throw}")
            print(f"{player_name} you lose!")
            break

start_battle()
player_choice_to_play_again = input("You want to play again? (y/n): ")

while True:
    if player_choice_to_play_again.lower() == "yes" or player_choice_to_play_again.lower() == "y":
        print("You decided to play again!")
        time.sleep(1.5)
        start_battle()
        player_choice_to_play_again = input("You want to play again? (y/n): ")
    if player_choice_to_play_again.lower() == "no" or player_choice_to_play_again.lower() == "n":
        print("You decided not to play anymore!")
        break