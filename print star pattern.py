
def print_pyramid(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=")
        for k in range(2*i-1):
            print("*", end="")
        print()
def print_inverted_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()
def print_right_angled_triangle(n):
    for i in range(1, n+1):
        # Printing stars
        for j in range(i):
            print("*", end="")
        print()

def print_diamond(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()
    for i in range(n-1, 0, -1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()
def print_hollow_pyramid(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i-1):
            if k == 0 or k == 2*i-2 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()
def main():
    n = int(input("Enter the number of rows for the patterns: "))
    
    print("\nPyramid Pattern:")
    print_pyramid(n)

    print("\nInverted Pyramid Pattern:")
    print_inverted_pyramid(n)

    print("\nRight-Angled Triangle Pattern:")
    print_right_angled_triangle(n)

    print("\nDiamond Pattern:")
    print_diamond(n)

    print("\nHollow Pyramid Pattern:")
    print_hollow_pyramid(n)
if __name__ == "__main__":
    main()
