# Exercise_134
# Luong Hoang Quan; 20203850
# Purpose: determines and displays the number of unique characters in a string entered by the user


s = str(input("Enter the string: "))
list = []
for ch in s:
    list.append(ch)
list1 = set(list)
print (f'{s} have {len(list1)} uniques')