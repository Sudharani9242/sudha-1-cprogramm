def gcd(a, b):
    min_num = min(a, b)
    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            return i  # Return the first common divison
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
