print('''''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to Tresuare Island.')
print("Your mission is to find the treasure.")

move = input('You are at a cross road. Where do you want to go? Type "left" or "right:" ').lower()

if move == "left":
    action = input('Now you have to decided , what you want to do , Type "wait" to wait for a boat or Type "swim" to swim across: ').lower()
    if action == "swim":
        print("Bad decision , A great shark has attacked you and you have died, the game is over. ")
    elif action =="wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose: ").lower()
        if color == "blue":
            print("You entered a room full of zombies, game over.")
        elif color == "red":
            print("Inside that room is the most feared vampire on the island, and he has turned you into his slave, game over.")
        elif color == "yellow":
            print("Congratulation You Win!, the treasure is your")
        else:
            print("Game Over!, Try Again!")
    else:
         print("Game Over!, Try Again!")
elif move == "right":
    print("You encountered the pirates and they have captured you, game over.")
else:
   print("Game Over!, Try Again!") 
