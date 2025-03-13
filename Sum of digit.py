
def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)  # Convert each digit back to an integer and add to the total
    return total
user_input = input("Enter a number: ")
if user_input.isdigit():
    result = sum_of_digits(user_input)
    print(f"The sum of the digits is: {result}")
else:
    print("Invalid input! Please enter a valid number.")
