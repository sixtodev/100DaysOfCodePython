print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is their name?") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names =  name1 + name2
lower_names =  combined_names.lower()
t= lower_names.count("t")
r= lower_names.count("r")
u= lower_names.count("u")
e= lower_names.count("e")
first_digit = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit =  l + o + v + e
score = str(first_digit) + str(second_digit)
love_score = int(score)

if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
