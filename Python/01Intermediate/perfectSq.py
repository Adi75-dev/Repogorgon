import math

# Taking the input from user
number = int(input("Enter the Number:   "))

root = math.sqrt(number)
print(root)
print(number)
if int(root + 0.5) ** 2 == number:  # 0.5 is added for Big numbers
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")
