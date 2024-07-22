import random
# 🚨 Remember to remove the print statement above when you submit.
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
len_list= len(names)
random_index = random.randint(0, len_list - 1)

name = names[random_index]
print(f"{name} is going to buy the meal today!")
