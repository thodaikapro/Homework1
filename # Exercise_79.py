# Exercise_79
# Luong Hoang Quan; 20203850
# Purpose: display maximum value encountered, along with the number of times the maximum valuewas updated during the process


import random

max_number = random.randint(1,100)
max_update = 0
for i in range(1,100):
    new_number = random.randint(1,100)
    if (new_number > max_number):
        max_number = new_number
        max_update += 1
        print (f'{new_number} <== Update')
    else:
        print (new_number)

print ('***\n')
print (f"The maximum value found was: {max_number}")
print (f"The maximum value was updated {max_update} times ")
