print("sudharani_27")
def access_elements(lst):
    if not lst:
        return "The list is empty."
    
    first = lst[0]
    last = lst[-1]
    middle = lst[len(lst)//2] if len(lst) % 2 != 0 else (lst[len(lst)//2 - 1], lst[len(lst)//2])
    
    return first, last, middle

my_list = [1, 2, 3, 4, 5]
first, last, middle = access_elements(my_list)
print(f"First: {first}, Last: {last}, Middle: {middle}")


 
