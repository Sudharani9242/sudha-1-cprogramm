def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) 
N = int(input("Enter the value of N: "))
print(f"The sum of squares of the first {N} natural numbers is: {sum_of_squares(N)}")
