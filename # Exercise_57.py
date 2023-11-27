# Exercise_57
# Luong Hoang Quan; 20203850
# Purpose: displays a message indicating whether or not it is a leap year.

x = int(input('Enter the year: '))

if (x % 400 == 0):
    print (f'{x} is leap year')

elif (x % 100 == 0):
    print (f'{x} is not a leap year')

elif (x % 4 == 0):
    print (f'{x} is leap year')

else:
    print (f'{x} is not a leap year')
