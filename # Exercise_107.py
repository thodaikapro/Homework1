# Exercise_107
# Luong Hoang Quan; 20203850
# Purpose: create a program that reads words from the user until the user enters a blank line


x = str(input())
list = []

while (x):
    list.append(x)
    x = str(input())
for i in sorted(set(list)):
    print (i)