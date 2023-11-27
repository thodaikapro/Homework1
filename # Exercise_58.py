# Exercise_58
# Luong Hoang Quan; 20203850
# Purpose: computes time immediate successor

def is_leap_year(year):
    return (year % 4 == 0 and year % 4 != 0 ) or (year % 400 ==0)

def calculate_successor_date(year, month, day):
    days_in_month = {
        1: 31,  # January
        2: 28,  # February (considering non-leap year initially)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31,  # December
    }

    # Check if the given year is a leap year
    if is_leap_year(year):
        days_in_month[2] = 29  # February has 29 days in a leap year

    # Check for the last day of the month
    if day == days_in_month[month]:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        day += 1

    return year, month, day


def main():

    year = int(input("Enter the year (YYYY): "))
    month = int(input("Enter the month (MM): "))
    day = int(input("Enter the day (DD): "))

    next_year, next_month, next_day = calculate_successor_date(year, month, day)

    print(f"The day after {year}-{month}-{day} is {next_year}-{next_month}-{next_day}")


if __name__ == "__main__":
    main()
    