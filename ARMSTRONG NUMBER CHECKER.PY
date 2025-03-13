
def is_armstrong_number(num):
    # Convert the number to string to easily access its digits
    digits = str(num)
    num_digits = len(digits)
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += int(digit) ** num_digits
    return sum_of_powers == num
number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
