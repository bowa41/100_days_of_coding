rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player = input("Please choose 'Rock', 'Paper', or 'Scissors' ").lower()
computer = random.randint(1,3)
if computer == 1:
  comp_choice = rock
elif computer == 2:
  comp_choice = paper
else:
  comp_choice = scissors
if player == "rock":
  player_choice = rock
elif player == "paper":
  player_choice = paper
elif player == "scissors":
  player_choice = scissors
else:
  print("You didn't pick a valid option!  I'll choose for you.")
  player_choice = comp_choice
print(f"You Chose:\n {player_choice}\n")
print(f"Computer Chose:\n {comp_choice}\n")
if player_choice == rock:
  if comp_choice == rock:
    print("You Tie!")
  elif comp_choice == paper:
    print("You Lose!")
  else:
    print("You Win!")
elif player_choice == paper:
  if comp_choice == rock:
    print("You Win!")
  elif comp_choice == paper:
    print("You Tie!")
  else:
    print("You Lose!")
else:
  if comp_choice == rock:
    print("You Lose!")
  elif comp_choice == paper:
    print("You Win!")
  else:
    print("You Tie!")