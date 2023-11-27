# Exercise_129
# Luong Hoang Quan; 20203850
# Purpose: main program that uses your function to simulate rolling two six-sided dice 1,000 times.


import random
def roll_2_dice():
    return random.randint(1, 6) + random.randint(1, 6)

# roll_dice_1(roll)
def main():
    rolls = 1000
    total_count = {i: 0 for i in range(2, 13)}
# rolls
    for _ in range(rolls):
        total = roll_2_dice()
        total_count[total] += 1
    print ("Total\tSimulated\tExpected")
    print ("\t  Percent  \t Percent")
    for total, count in total_count.items():
        simulated_percent = (count/rolls) * 100
        expected_percent = (6 - abs(7 - total)) / 36 * 100
        print(f"{total:5} {simulated_percent:11.2f} {expected_percent:14.2f}")

if __name__ == "__main__":
    main()
