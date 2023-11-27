# Exercise_76
# Luong Hoang Quan; 20203850
# Purpose: display the prime numbers


x = int(input('Enter a integer number: '))

if (x < 2):
    print ('Error')

def prime_factorization(n):
    factor = 2
    factors = []
    while factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n //= factor
        else:
            factor += 1

    return factors

factors = prime_factorization(x)       

for i in factors:
    print (i)