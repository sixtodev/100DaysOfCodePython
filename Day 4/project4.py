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
game= (rock, paper,scissors)
player_1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
if (player_1 >=3 or player_1 < 0):
    print('You typed an invalid number , you lose!')
else:
    print(game[player_1])
    print("Computer Chose:")
    player_2 = random.randint(0, 2)
    print (game[player_2])

    if(player_1 == player_2):
        print("It's a draw")
    elif(player_1 == 0) and (player_2 ==2):
        print("You Win")
    elif(player_2 == 0) and (player_1 ==2):
        print("You Lose")
    elif(player_2 > player_1):
        print("You Lose")
    elif(player_1 > player_2):
       print("You Win")


