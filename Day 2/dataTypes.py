#integer
#examples of integers   1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#larger integers
123_456_789 # we use underscores to make large numbers more readable

#floats
3.1459


#booleans
True 
False

#strings
"Hello World"

#type function

print(type(6)) #int
print(type(2.5)) #float
print(type("Hello")) #str
print(type(True)) #bool

#type conversion or type casting
#convert int to string
num = 123
print(type(num))
num = str(num)
print(type(num))

#convert string to int
num = "123"
print(type(num))
num = int(num)
print(type(num))

#convert string to float
num = "123.5"
print(type(num))
num = float(num)
print(type(num))

num_char = len(input("What is your name?"))
new_num = str(num_char)
print("Your name has " + new_num + " characters.")


#exercise

two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(sum)