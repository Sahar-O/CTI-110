# Sahar Olaya 
# 2 March 2025
# P2HW2
# The program collects and analyzes test grades

# Pseudocode:
# 1. Ask the user to enter grades for six modules.
# 2. Store the grades in a list.
# 3. Calculate the lowest, highest, sum, and average of the grades.
# 4. Display the results with proper formatting.

# A list to store grades
grades = []

# Get grades from the user
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Calculate required values
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest}")
print(f"Highest Grade:     {highest}")
print(f"Sum of Grades:     {total}")
print(f"Average Grade:     {average:.2f}")
print("--------------------------------")