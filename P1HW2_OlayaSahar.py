# Sahar Olaya 
# 2/13/2025
# P1HW2
# A program that does some basic math on numbers that are entered.


print("This program calculates and displays traveil expenses")

# Get user input information
Budget = int(input("Enter Budget:"))
print()
Travel_Destination = input("Enter your travel destination:")
print()
Gas_expenses = int(input("How much do you think you will spend on gas?"))
print()
Hotel_expenses = int(input("Approximately, how much will you need for accomodation/hotel?"))
print()
Food_expenses = int(input("Last, how much do you need for food?"))
print()


# Display travel expenses and destination
print("-----------Travel Expenses-----------")
print("Location:",Travel_Destination)
print("Initial Budget:",Budget)
print()
print("Fuel:",Gas_expenses)
print("Accomodation:",Hotel_expenses)
print("Food:",Food_expenses)
print()

#Math calculation
Results = Budget - Gas_expenses - Hotel_expenses - Food_expenses

print("Remaining Balance:",Results)

