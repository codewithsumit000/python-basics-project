import random
import time

print("Do you want to roll the dice?")
person_input = input("Enter 'yes' or 'no': ").lower()

if person_input == "yes":
    print("The dice is rolling... wait for the result.")
    print("The opponent's dice is also rolling at the same time.")
    time.sleep(1)

    print("Let's see who will win!")
    time.sleep(2)

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    if player_roll > computer_roll:
        print(f"Your dice is {player_roll} and computer's dice is {computer_roll}. You win!")
    elif player_roll == computer_roll:
        print(f"Your dice is {player_roll} and computer's dice is {computer_roll}. It's a draw!")
    else:
        print(f"Your dice is {player_roll} and computer's dice is {computer_roll}. Computer wins!")
else:
    print("You can try the game, it's interesting!")
