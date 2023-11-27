# Exercise_90
# Luong Hoang Quan; 20203850
# Purpose: write a function named isInteger that determines whether or not the characters in a string represent a valid integer


def isInteger(s):
    s = s.strip()  # Remove leading and trailing whitespaces

    if len(s) == 0:
        return False  # Empty string is not a valid integer

    if s[0] in ['+', '-']:
        return s[1:].isdigit() if len(s) > 1 else False
    else:
        return s.isdigit()

def main():
    user_input = input("Enter a string to check if it represents an integer: ")
    result = isInteger(user_input)

    if result:
        print("The entered string represents an integer.")
    else:
        print("The entered string does not represent an integer.")

if __name__ == "__main__":
    main()