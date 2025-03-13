
def count_digits(number):
    number_str = str(abs(number))  # Using abs() to ignore negative sign
    return len(number_str)
number = int(input("Enter a number: "))
digit_count = count_digits(number)
print(f"The number of digits in {number} is: {digit_count}")
