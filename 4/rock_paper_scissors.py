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

#Write your code below this line 👇
ascii = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"User {ascii[user]}")
computer = random.randint(0, 2)
print(f"COMPUTER {ascii[computer]}")
if user > 2 or user < 0:
    print("You chose an invalid number")
if user == 0 and computer == 2:
    print(f"You Win!")
elif computer > user:
    print("You Lose!")
elif user > computer:
    print("You Win!")
elif computer == user:
    print("Draw!")
