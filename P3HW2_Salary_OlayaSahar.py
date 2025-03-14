# Sahar Olaya
# March 14, 2025
# P3HW2 
# This program calculates an employee's regular pay, overtime pay, and gross pay based on hours worked.

# Pseudocode:
# Ask the user for the employee's name, hours worked, and pay rate.
# Check if the employee worked more than 40 hours:
#    - If yes, calculate overtime hours and pay (1.5 times pay rate).
#    - Otherwise, there is no overtime.
# Calculate regular pay.
# Calculate gross pay (regular pay + overtime pay).
# Display all details 

# Get user input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize variables
overtime_hours = 0
overtime_pay = 0
regular_hours = min(hours_worked, 40)  # Regular hours capped at 40

# Check for overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

# Calculate regular pay
regular_pay = regular_hours * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results 
print("\n-------------------------------------")
print(f"Employee Name: {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("--------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<15.1f}{overtime_hours:<15.1f}{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}")

