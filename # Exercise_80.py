# Exercise_80
# Luong Hoang Quan; 20203850
# Purpose: creating a program that simulates several series of coin flips


import random

def flip_coin():
    sum_H = 0
    sum_T = 0
    flips = 0
    list = []
    while sum_H < 3 and sum_T < 3:
        outcome = random.choice(['H', 'T'])
        list.append(outcome)
        flips +=1

        if (outcome == 'H'):
            sum_H += 1
            sum_T = 0
        else:
            sum_T +=1
            sum_H = 0
    
    print(f"{' '.join(map(str, list))} ({flips} flips)")
        # print(f"\nNumber of flips needed: {flips}\n")
    return flips

def main():
    total_flips = 0
    simulations = 10

    for _ in range(simulations):
        total_flips += flip_coin()

    average_flips = total_flips / simulations
    print(f"On average, {average_flips:.2f} flips were needed.")

if __name__ == "__main__":
    main()