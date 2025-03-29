# Sahar Olaya
# 3/29/2025
# P4HW1
# Edit and enhance existing programs


# Pseudocode:
# 1. Initialize totals and employee count.
# 2. Loop: Get employee details or exit on "Done".
# 3. Calculate regular and overtime pay.
# 4. Update totals and display individual results.
# 5. Display summary of all employees.

# Initialize variables
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

while True:
    employee_name = input("Enter employee's name (or 'Done' to terminate): ")
    if employee_name == "Done":
        break
    
    pay_rate = float(input(f"Enter {employee_name}'s pay rate: "))
    hours_worked = float(input(f"Enter hours worked by {employee_name}: "))
    
    # Calculate pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
    
    gross_pay = regular_pay + overtime_pay
    
    # Accumulate totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    num_employees += 1
    
    print("\n-----------------------------------------------------------------------------------------------")
    print(f"Employee Name: {employee_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("--------------------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<15.1f}{overtime_hours:<15.1f}{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}")

# Final Summary Output
print("\nTotal Number of Employees Entered:", num_employees)
print("Total Overtime Pay:", total_overtime_pay)
print("Total Regular Pay:", total_regular_pay)
print("Total Gross Pay:", total_gross_pay)
