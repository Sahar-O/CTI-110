# Sahar Olaya 
# 3/4/2025
# P3LAB
# Using if/else to display coin combinations

# Get the amount of money from user as float 
initial_amount = float(input("Enter the amount of money as a float: $"))

# Convert amount into an integer
amount = int(round(initial_amount * 100, 2))

#print(amount)

# Determine num_dollars in amount
num_dollars = amount // 100
#print(f"Num Dollars: {num_dollars}")
#Subtract num_dollars from amount
amount = amount - (num_dollars * 100)
#print(f"New Amount: {amount}")

# Determine num_quarters in amount
num_quarters = amount // 25
#print(f"Num Quarters: {num_quarters}")
#Subtract num_quarters from amount
amount = amount - (num_quarters * 25)
#print(f"New Amount: {amount}")

# Determine num_dimes in amount
num_dimes = amount // 10
#print(f"Num Dimes: {num_dimes}")
#Subtract num_dimes from amount
amount = amount - (num_dimes * 10)
#print(f"New Amount: {amount}")

# Determine num_nickels in amount
num_nickels = amount // 5
#print(f"Num Nickels: {num_nickels}")
#Subtract num_nickels from amount
amount = amount - (num_nickels * 5)
#print(f"New Amount: {amount}")

num_pennies = amount

#print()
#print()
#print()

#print("here is the most efficient coin combo")
print(f"${initial_amount:.2f}")

# Print No Change if amount entered is 0.00
if initial_amount == 0.00:
    print("No Change")

# Display coins needed with proper grammar
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarters")
    else:
        print(f"{num_quarters} Quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")


