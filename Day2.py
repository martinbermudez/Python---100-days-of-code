#BMI Calculator
"""
print("BMI Calculator\n")
height = float(input("Enter your height in meters: \n"))
weight = float(input("Enter your weight in kilograms: \n"))

bmi= int(weight/(height**2))
print("Your BMI is:", bmi)
"""

#Tip Calculator
tot_bill = float(input("What was the total bill?\n"))
per_tip = float(input("What percentaje tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))

per = (per_tip/100)+1

tot_wtip = round((tot_bill/people) * per,2)

print("Each person should pay: $",tot_wtip)