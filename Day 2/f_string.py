#f-string
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")# we use f-string to insert variables into strings.

#exercise

age = input("What is your current age?")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

maximum_year = 90
left_year = maximum_year - int(age)
weeks_in_one_year= 52
weeks_left = left_year * weeks_in_one_year
print(f"You have {weeks_left} weeks left.")