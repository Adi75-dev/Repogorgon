# To check whether a letter is present in the list
names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print('Not found')


# x = int(input("Please Enter an Integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


# Measure Strings
words = ['Cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    else:
        print("Found a number", num)

c = input("Enter a positive integer: ")
r = (int(c) % 2)
if r == 0:
    print('Even')
elif r == 1:
    print("Odd")
else:
    print("Not a valid input")


i = 1
while i <= 5:
    print('Adi')
    i = i+1
