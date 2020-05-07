students_count = 1000
rating = 4.99
is_published = False
course_name = "Python"
x = 1
y = 2
x, y = 1, 2
x = y = 1
print(x, y)  # value of X & y changes with each declaration
print(type(students_count))
print(type(course_name))

# Type Annotations
age = 20
age = "Python"
print(age)

# Mutable & Immutable types
x = 1  # Integers are Immutable i.e-It's Value doesn't change
print(id(x))

x = x+1
print(id(x))

y = [1, 2, 3]  # Arrays and all other data types are mutable
print(id(y))
y.append(4)
print(id(y))


# Strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])  # This line can also be written as:
print(course[:3])
