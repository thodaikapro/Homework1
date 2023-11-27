# Exercise_104
# Luong Hoang Quan; 20203850
# Purpose: that reads integers from the user and stores them in a list

x = int(input("Enter a number: "))
list = []

# print (x)
while(x != 0):
    list.append(x)
    x = int(input('Enter a number: '))
else:
    print (sorted(set(list)))