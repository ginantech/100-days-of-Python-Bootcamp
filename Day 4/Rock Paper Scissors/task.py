import random

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

game_choices = [rock, paper, scissors]
print("let's play a game!")
players_choice = int(input("\nWhat do you choose? 0 for rock, 1 for paper, or 2 for scissors?\n"))


if players_choice >= 0 and players_choice <= 2:
    print(game_choices[players_choice])


computers_choice = random.randint(0, 2)
print("Computers Choice:")
print(game_choices[computers_choice])


if players_choice >= 3 or players_choice < 0:
    print("You typed an invalid number. You lose!")
elif players_choice == 0 and computers_choice == 2:
    print("You win!")
elif computers_choice == 0 and players_choice == 2:
    print("You lose!")
elif computers_choice > players_choice:
    print("You lose!")
elif players_choice > computers_choice:
    print("You win!")
elif computers_choice == players_choice:
    print("It's a draw!")










