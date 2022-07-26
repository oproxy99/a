print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction=input("You are at a crossroad. Where do you want to go? Left or Right\n")

if direction=="Left":
    print("You fell into a hole. Game Over")

elif direction=="Right":
    opt1=input("You have come to a lake. There is an island in the middle of the lake. Type 'Swim' to swim across or Type 'Wait' to wait for a boat.\n")

    if opt1=="Swim":
        print("You tried to swim but died due to exhaustion. Game Over.")

    elif opt1=="Wait":
        print("You arrived at the island unharmed.")
        door=input("There are three doors infront of you. Choose Red, Blue or Yellow.\n")

        if door=="Red":
            print("You fell into a pool of lava. Game Over.")

        elif door=="Blue":
            print("You were killed by a yeti. Game Over.")

        elif door=="Yellow":
            print("You found the treasure. CONGRAGULATIONS!!")

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")

else:
    print("Invalid choice")
        
