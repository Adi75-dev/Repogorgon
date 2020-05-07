first = "Aditya"
last = "Mhambrey"
full = first+" "+last
print(full)
full = f"{first} {last} {2+2} {len(first)}"
print(full)
course = "  Python Programming"
print(course.upper())
print(course.lower())
print(course.title())  # First Letter of every Word is capital
print(course.strip())  # Getting rid of white space
print(course.rstrip())  # Getting rid of white space from right similar for Left
print(course.find("Pro"))  # Same as JS, -1 for wrong case
print(course.replace("P", "-"))
print("Programming" in course)
print("Programming" not in course)
