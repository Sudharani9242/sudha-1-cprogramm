print("sudharani_27")
def remove_element(lst, element):
    try:
        lst.remove(element)  
        print(f"Element '{element}' removed successfully.")
    except ValueError:
        print(f"Element '{element}' not found in the list.")
my_list = [1, 2, 3, 4, 5, 6, 3, 7]
print("Original list:", my_list)
remove_element(my_list, 3)
print("Updated list:", my_list)
