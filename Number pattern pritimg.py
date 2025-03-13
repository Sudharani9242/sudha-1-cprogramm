
def print_pascals_triangle(n):
    for line in range(n):
        for i in range(n - line - 1):
            print(" ", end="")
        num = 1
        for i in range(line + 1):
            print(num, end=" ")
            num = num * (line - i) // (i + 1)
        print()
def print_floyds_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
def print_square_number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()
def print_right_angled_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
def print_pyramid_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i * 2):
            print("*", end="")
        print()
def main():
    print("Pascal's Triangle:")
    print_pascals_triangle(5)

    print("\nFloyd's Triangle:")
    print_floyds_triangle(5)

    print("\nSquare Number Pattern:")
    print_square_number_pattern(5)

    print("\nRight-Angled Triangle Pattern:")
    print_right_angled_triangle(5)

    print("\nPyramid Pattern:")
    print_pyramid_pattern(5)

if __name__ == "__main__":
    main()
