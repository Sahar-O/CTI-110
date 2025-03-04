# Sahar Olaya 
# 3/4/2025
# P3LAB
# Using if/else to display coin combinations

# Get the amount of money from user as float 
amount = float(input("Enter the amount of money as a float: $"))

# Convert amount into an integer
amount = int(round(amount * 100, 2))

print(amount)

# Determine num_dollars in amount
num_dollars = amount // 100
print(f"Num Dollars: {num_dollars}")
#Subtract num_dollars from amount
amount = amount - (num_dollars * 100)
print(f"New Amount: {amount}")

# Determine num_quarters in amount
num_quarters = amount // 25
print(f"Num Quarters: {num_quarters}")
#Subtract num_quarters from amount
amount = amount - (num_quarters * 25)
print(f"New Amount: {amount}")

# Determine num_dimes in amount
num_dimes = amount // 10
print(f"Num Dimes: {num_dimes}")
#Subtract num_dimes from amount
amount = amount - (num_dimes * 10)
print(f"New Amount: {amount}")

# Determine num_nickels in amount
num_nickels = amount // 5
print(f"Num Nickels: {num_nickels}")
#Subtract num_nickels from amount
amount = amount - (num_nickels * 5)
print(f"New Amount: {amount}")

num_pennies = amount