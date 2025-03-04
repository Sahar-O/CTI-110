# Get user's age 
age = int(input("Enter your age : "))

# if/else statemnt to determine senior status
if age >= 65:
    print(f"You are a senior at age {age}")
else:
    print(f"You are not a senior you are only {age}")


if age >= 65:
    life_stage = "Senior"
elif age >= 18 and age < 65:
    life_stage = "Adult"
elif age < 18 and age >=0:
    life_stage = "Child"
else:
    life_stage = "INVALID"

print(f"At age {age}, your life stage is {life_stage}")