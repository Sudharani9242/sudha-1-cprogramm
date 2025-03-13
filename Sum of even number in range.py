def sum_of_even_numbers(start, end):
    total_sum = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            total_sum += number
    
    return total_sum
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
result = sum_of_even_numbers(start, end)
print(f"The sum of all even numbers between {start} and {end} is {result}.")
