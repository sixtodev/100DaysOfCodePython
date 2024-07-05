# bill calculator


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tips= int(input("How much tip would you like to give? 10, 12, or 15? "))
split= int(input("How many people to split the bill? "))


tip_porcentage = tips / 100  + 1 
total_pay= bill * tip_porcentage
# total_per_person = round(total_pay / split, 2)  # here we are using  round function
total_per_person = total_pay / split
final_amount = "{:.2f}".format(total_per_person)  # here we are using format function

# print(f"Each person should pay: ${total_per_person}")
print(f"Each person should pay: ${final_amount}")