
def gcd(a, b):
    while b:
        a, b = b, a % b
    return 0
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = lcm(num1, num2)
print(f"The Least Common Multiple of {num1} and {num2} is {result}")
