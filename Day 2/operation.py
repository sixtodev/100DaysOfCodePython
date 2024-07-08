#mathematical operations

def add(a,b):
    return a+b  
def subtract(a,b):
    return a-b
def multiply(a,b):
    return
def divide(a,b): # during division, the result is always a float
    return a/b
def modulus(a,b):
    return  a%b
def exponent(a,b): 
    return a**b




suma = add(2,3)
print(suma)


#exercise

# 1st input: enter height in meters e.g: 1.65
height = input("enter height in meters e.g: 1.65\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("enter weight in kilograms e.g: 72\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
f_height = float(height)
f_weight = int(weight)
bmi = f_weight / pow(f_height,2)
print(round(bmi,2))

#rounding numbers1.65
print(round(8/3, 2)) # 2 decimal places
print(round(2.6666666666666665, 2)) # 2 decimal places
print(round(2.6666666666666665, 3)) # 3 decimal places

   #floar division
print(8//3) # 2 this is floar division, it returns an integer not a float
print(type(8//3)) # int

#shorthand notation
score = 0
score += 1 # instead of score = score + 1
score -= 1 # instead of score = score - 1
score *= 2 # instead of score = score * 2
score /= 2 # instead of score = score / 2
print(score)







