#Odd or Even
"""
num = int(input("Which number do you want to check?\n"))

if num%2 ==0:
    print("The number ", num, " is even.")
else:
    print(f"The number {num} is odd.")
"""

#BMI Calculator v2

print("BMI Calculator v2")
height = float(input("Enter your height in mts\n"))
weight = float(input("Enter your weight in kg\n"))

bmi = round(weight / (height**2),2)

if bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi > 30:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 25:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 18.5:
    print(f"Your BMI is {bmi}, you have normal weight.")
else:
    print(f"Your BMI is {bmi}, you are underweight.")

#Treasure Island

print("Welcome to Treasure Island. Your mission is to find the treasure!")
print('''******************************************************************************
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
*******************************************************************************''')
d1 = input("You see two paths, which one you chose? Left or Right?\n").lower()
if d1 == "left":
    d2 = input("You encounter a lake! Would you like to swim or wait for a boat?\n").lower()
    if d2 == "wait":
        d3 = input("You crossed the lake with no worries! But now, you see 3 doors...\nBlue, Red and Yellow are the colors. \nWhich one should you chose?").lower()
        if d3 == "red":
            print("You entered the red door... sadly you caught on fire and died burnt. GAME OVER.")
        elif d3 == "blue":
            print("You entered the blue door... saddly you encounter a beast that eat you up!. GAME OVER.")
        else:
            print("You entered the yellow door...\nIt's dark and you cannot see anything but suddenly there is a bright light at the end of the room!\nYOU FOUND THE TREASURE!")
    else:
        print("You were devoured by a trout. GAME OVER.")
else:
    print("You fall into a hole. GAME OVER.")
