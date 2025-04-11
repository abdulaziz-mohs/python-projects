print("Welcome to the tip calculator!!")
bill=float(input("What is the current bill?"))
bill_percentage=float(input("What percentage of the bill you want to give?10, 12 or 15? "))
num_people=int (input("How many people to split the bill?"))

total=bill+(bill*bill_percentage/100)
print(f"\n Each person should pay {round(total/num_people,2)}")