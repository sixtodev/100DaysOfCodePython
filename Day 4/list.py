# list is a type of data structure

#examples of list

fruits = ["banana", "apple", "orange" , "Cherry"] # can be any data type or mix, you aslo can data in your list

#example
fruits[2] = "palta"

print(fruits)


# also you can add more item in your end of the list with the function append.

fruits.append("apple")
print(fruits)


# tipical error  : IndexError: list index out of range
# to solve this error you must to call the list (len - 1)

#nested list
# dirty_dozen=["Strawberries","Spinach","Kale","Nectarines","Apples", "Grapes", "Peaches","Cherries", "Pears","Celery","Potatoes"]

fruits=["Strawberries", "Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetable=["Spinach","Kale","Tomatoes","Celery","Potatoes"]

dirty_dozen= [fruits,vegetable]  # nested list

print(dirty_dozen)
print(fruits[-5])

fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)