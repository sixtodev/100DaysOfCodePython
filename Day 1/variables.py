# variables


name = input("What is your name?")
length = len(name)
print( length)


#exercise swap values of variables

# There are two variables, a and b
a = input("Enter a value for a: ")
b = input("Enter a value for b:")
# Create a third variable to help switch the values
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

#make code readable , use descriptive variable names , in python use snake_case
# examples
# num_of_students = 10
# num_of_classes = 5
# num_of_teachers = 3
# my_first_name = "Sixto"