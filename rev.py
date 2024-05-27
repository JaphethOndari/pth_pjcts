def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    print(s)
    return s == s[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
