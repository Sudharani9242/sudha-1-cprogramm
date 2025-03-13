print("sudharani_27")
my_set = set()
def add_element(element):
    my_set.add(element)
    print(f"Element {element} added to the set.")
    
def remove_element(element):
    if element in my_set:
        my_set.remove(element)
        print(f"Element {element} removed from the set.")
    else:
        print(f"Element {element} not found in the set.")
        
add_element(10)
add_element(20)
add_element(30)

remove_element(20)
remove_element(40)  
print("Current set:", my_set)


