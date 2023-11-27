# Exercise_83
# Luong Hoang Quan; 20203850
# Purpose: reads the number of items purchased from the user and displays the shipping charge.


x = int(input('Enter the number of items: '))

if (x == 1):
    charge = 10.95
else:
    charge = (x - 1) * 2.95 + 10.95

print (f'Shipping charge is: {charge:.2f}$')