print("sudharani_27")
def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]
result = is_palindrome("A man a plan a canal Panama")
print(result)
output
sudharani_27
true
