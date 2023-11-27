# Exercise_77
# Luong Hoang Quan; 20203850
# Purpose: converts a binary (base 2) number to decimal (base 10).


def find_dec(binary_num):
    dec_num = 0

    i = 0
    for digit in binary_num:
        digit = int(digit)
        dec_num = dec_num + (digit * pow(2, i))
        i += 1
    return dec_num

def main():
    num = input('Enter the binary number: ')
    if not all (bit in '01' for bit in num):
        print ('Error')
    else:
        dec = find_dec(num)
        print (f'Decimal number of {num} is {dec}')

if __name__ == '__main__':
    main()
