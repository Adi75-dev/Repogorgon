name = "Adi"  # to check if given string is an empty string
if not name.strip():
    print("Name is Empty")

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# This code can also be written as:
if 18 <= age < 65:
    print("Eligible")

# Ternary Operator
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
