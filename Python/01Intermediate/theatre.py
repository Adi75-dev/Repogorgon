x = int(input('Enter your Age:  '))
print('****************')
for i in range(0, 1):
    if x >= 18:
        print('You can watch content with R-rating')
    elif x >= 13:
        print('You can watch movies under parental guidance ')
    else:
        print('Cartoons permitted')

print('     Thanks!     ')
