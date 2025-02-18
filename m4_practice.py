# Sahar Olaya
# Get the name of an item from the user 
product = input("What are you purchasing?")
cost = float(input(f"How much do(es) the {product.upper()} cost? "))

# Display the data back to user using a formatted string 
print(f"You are buying {product} and it cost ${cost:.2f}")


with_tax = cost + (cost * 0.07) 
print(f"with tax, the {product} costs ${with_tax:.2f}")