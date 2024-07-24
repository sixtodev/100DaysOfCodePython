#password generator 3 way to create this program

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



letters_pass= (random.sample(letters,nr_letters))
symbols_pass = (random.sample(symbols,nr_symbols))
numbers_pass = (random.sample(numbers,nr_numbers))

password = letters_pass + symbols_pass + numbers_pass
random.shuffle(password)

new_pass = ''.join(password)
print(f"You password is: {new_pass}")


# this approach is more efficient, but sample function dont allow to add duplicate 
#---------------------------------------------------------------------------#

password_list = []

for char in range(1,nr_letters +1):
    password_list += random.choice(letters)
for char in range(1,nr_symbols +1):
    password_list += random.choice(symbols)
for char in range(1,nr_numbers +1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"You password is: {password}")

# this approach is more flexible with random.choice 

#----------------------------------------------------------------
# this final option is better because is more flexible and still is efficient in terms of execution time
letters_pass = [random.choice(letters) for _ in range(nr_letters)]
symbols_pass = [random.choice(symbols) for _ in range(nr_symbols)]
numbers_pass = [random.choice(numbers) for _ in range(nr_numbers)]

password = letters_pass + symbols_pass + numbers_pass
random.shuffle(password)

new_pass = ''.join(password)
print(f"Your password is: {new_pass}")