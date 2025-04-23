import random
# making list of choice for computer
items = ['rock', 'paper', 'scissors']
computer = random.choice(items)

# User input
print("""Which move do you want to choose?
1. Rock
2. Paper
3. Scissors
""")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    people = 'rock'
elif choice == '2':
    people = 'paper'
elif choice == '3':
    people = 'scissors'
else:
    print("Invalid input. Please enter 1, 2, or 3.")
    exit()

print(f"\nYou chose: {people}")
print(f"Computer chose: {computer}")

if people == computer:
    print("It's a draw! Play again.")
elif ((people == "rock" and computer == "scissors") or  (people == "paper" and computer == "rock") or   (people == "scissors" and computer == "paper")):
     print("You are the winner! ")
else:
    print("Computer is the winner! ")
    



    
