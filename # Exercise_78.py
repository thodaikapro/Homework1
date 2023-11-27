# Exercise_78
# Luong Hoang Quan; 20203850
# Purpose: converts a decimal (base 10) number to binary (base 2).


num_dec = input("Enter a decimal: ")
num = int(num_dec)
if (num == 0):
    num_bi = 0
def convert_bin(num):
    num = int(num)
    list = []
    # if (num > 0):
    while (num >= 1):
        i = num % 2 
        list.append(i)
        num = num//2
    else:
        return (''.join(map(str, list)))
    
def main():

    if (num == 0):
        num_bi = 0
    else:
        num_bi = convert_bin(num_dec)
    print (f'Binary number of {num_dec} is {num_bi}')

if __name__ == '__main__':
    main()
    