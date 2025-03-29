# Sahar Olaya
# 2/25/2025
# P4HW1
# Edit and enhance existing programs

# Get the number of scores from the user
num_scores = int(input("How many scores do you want to enter: "))

# Create an empty list to store scores
scores_list = []

# Loop to get user input for scores
for each in range(num_scores):
    score = int(input(f"Enter score #{each + 1}: "))
    

    # Validate input to ensure score is between 0 and 100
    while score < 0 or score > 100:
        print("INVALID score entered! Score must be between 0 and 100.")
        score = int(input(f"Enter score #{each + 1} again: "))
    
    scores_list.append(score)



print("-----------------------Results-------------------------")
# Get the lowest score in the list
lowest_score = min(scores_list)
print("Lowest score:", lowest_score)

# Remove the lowest score from the list
scores_list.remove(lowest_score)

# Print the list of scores to ensure correctness
print("Modified List:", scores_list)


# Calculate the average of the remaining scores
if len(scores_list) > 0:
    average_score = sum(scores_list) / len(scores_list)
else:
    average_score = 0


print("Scores Average:", format(average_score, ".2f"))
# Determine the letter grade based on the average score
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("Grade:", letter_grade)

print("-------------------------------------------------------")