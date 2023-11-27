# Exercise_27
# Luong Hoang Quan; 20203850
# Purpose: Computes the body mass index (BMI) of an individual.


def main():
    unit_selection = input('Enter the unit system (imperial/metric): ')
    
    if (unit_selection.lower() == 'imperial'):
        weight = float(input('Enter the weight in pounds: '))
        height = float(input('Enter the height in inches: '))
    
    elif (unit_selection.lower() == 'metric'):
        weight = float(input('Enter the weight in kilograms: '))
        height = float(input('Enter the height in meters: '))

    else:
        print ("Invalid Unit")
        return
    bmi = calculator_bmi(weight, height, unit_selection)
    print (f'Calculator BMI of body is: {bmi: .2f}')

def calculator_bmi(weight, height, unit_system):
    if (unit_system.lower() == 'imperial'):
        bmi = weight/(weight * height)* 703
    elif (unit_system.lower() == 'metric'):
        bmi = weight/(weight * height)  
    else:
        return "Invalid unit. Please choose 'imperial' or 'metric' "
    return bmi

if __name__ == '__main__':
    main()