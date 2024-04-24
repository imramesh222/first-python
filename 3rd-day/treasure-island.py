print('''*******************************************************************************
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
*******************************************************************************''')
print("Welcome to the treasure Island.\nYour mossion is to find the treasure")
# choice1=input("Left or Right: ").lower()
# choice2=input("swim or wait: ").lower()
# choice3=input("Red, Blue or Yellow: ").lower()
# print("you're at a cross road. Where do you want to go? Left or Right: ")
# if choice1 == "right":
#   print("Game Over!")
# else:
#   print("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. type 'swim' to swim across: ")
#   if choice2 == "swim":
#     print("Game Over!")
#   else:
#     print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? Red, Yellow or Blue: ")
#     if choice3=="red" and choice3=="blue":
#       print("Game Over!")
#     else:
#       print("You win! You found the treasure!")




# choice1=input("you are at a crossroad, wher do you want to go? type left or right.").lower()
# if choice1=="left":
#   choice2=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. type 'swim' to swim across: ").lower()
#   if choice2=="wait":
#     choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? Red, Yellow or Blue: ").lower()
#     if choice3=="yellow":
#       print("You win! You found the treasure!")
#     elif choice3=="red" or choice3=="blue":
#       print("You choose the wrong door.\nGame Over!\nTry again later")
#     else:
#       print("Door does not exist, please choose between given optios, Game Over")
#   else:
#     print("You are drown.\nGame Over!\nTry again later")
# else:
#   print("You choose wrong way.Game Over!\nTry again later")

    
choice1 =input("choose left or right\n").lower()
if choice1=="left":
  choice2=input("Choose swim or wait\n").lower()
  if choice2=="wait":
    choice3=input("Choose red, blue or yellow\n").lower()
    if choice3=="red":
      print("You choose wrong door.\nTry again later")
    elif choice3=="blue":
      print("You choose wrong door.\nTry again later")
    elif choice3=="yellow":
      print("You win! You found the treasure!")
    else:
      print("You type incorectly.\nTry again later")
  else:
    print("You are drown.\nGame Over!\nTry again later")
else:
  print("You choose wrong way.Game Over!\nTry again later")
  