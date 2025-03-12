import math

def calculate_square_root(n):
    """Calculate the square root of a number."""
    return math.sqrt(n)
def calculate_factorial
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return math.factorial(n)

def calculate_sine(n):
    return math.sin(n)
def main():
    number = float(input("Enter a number: "))
    square_root = calculate_square_root(number)
    factorial = calculate_factorial(int(number))  # Factorial works only for integers
    sine = calculate_sine(number)
    print(f"The square root of {number} is: {square_root}")
    print(f"The factorial of {int(number)} is: {factorial}")
    print(f"The sine of {number} (in radians) is: {sine}")

if __name__ == "__main__":
    main()
