# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()


# fib(2000)


nterms = int(input("How many terms? "))

n1, n2, count = 0, 1, 0

if nterms <= 0:
    print('Enter positive integer')
elif nterms == 1:
    print("Fibonnaci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
