
number = int(input("Enter an integer: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
