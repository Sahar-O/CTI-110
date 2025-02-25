# Sahar Olaya
# 2/25/2025
# P2HW1
# Changing how results are displayed


print("This program calculates and displays traveil expenses")

# Get user input information
Budget = int(input("Enter Budget: "))
print()
Travel_Destination = input("Enter your travel destination: ")
print()
Gas_expenses = int(input("How much do you think you will spend on gas? "))
print()
Hotel_expenses = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
Food_expenses = int(input("Last, how much do you need for food? "))
print()


# Display travel expenses and destination
print("-" * 15, "Travel Expenses", "-" * 15)
print(f"{'Location:':<20} {Travel_Destination}")
print(f"{'Initial Budget:':<20} ${Budget:.2f}")
print(f"{'Fuel:':<20} ${Gas_expenses:.2f}")
print(f"{'Accomodation:':<20} ${Hotel_expenses:.2f}")
print(f"{'Food:':<20} ${Food_expenses:.2f}")
print()
print("-" * 50)

#Math calculation
Results = Budget - Gas_expenses - Hotel_expenses - Food_expenses

print(f"{'Remaining Balance:':<20} ${Results:.2f}")
