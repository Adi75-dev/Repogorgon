import math

name = (input("Enter your Name:  "))
std = (int(input("Enter your Standard:  ")))
div = (input("Enter your Div:   "))
roll_no = (int(input("Enter your roll no:  ")))
if std >= 10:
    print("Higher secondary")
elif std >= 8:
    print("Secondary")
else:
    print("Primary")
    print(name, '', div, '', std, '', roll_no)
