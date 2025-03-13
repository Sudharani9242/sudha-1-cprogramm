print("sudharani_27")
def count_occurrences(lst, element):
    return lst.count(element)
my_list = [1, 2, 3, 4, 5, 1, 2, 1, 3]
element_to_count = 1

occurrences = count_occurrences(my_list, element_to_count)

print(f"The element {element_to_count} occurs {occurrences} times in the list.")
