print("sudharani_27")
def check_element_in_set(element, my_set):
    if element in my_set:
        return True
    else:
        return False

my_set = {1, 2, 3, 4, 5}
element = 2

if check_element_in_set(element, my_set):
    print(f"The element {element} exists in the set.")
else:
    print(f"The element {element} does not exist in the set.")
