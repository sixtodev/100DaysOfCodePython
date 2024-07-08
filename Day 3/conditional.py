# if condition:
#     do this
# else:
#     do this
    
    
print("Welcome to the rollercoaster!")


height =  int(input("What is your height in cm "))

if height >=  120:
    print("You can ride")
    age = int(input("What is your age "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You can not ride")
    
# exercises

# Which number do you want to check?
number = int(input("What number do you wnat to check "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
#nested if statement

# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

