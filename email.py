import re

pattern = r"[a-zA-Z0-9]+@[A-Za-z0-9]+\.(com|ke)"

user_input = input("Enter an email address: ")

if re.match(pattern, user_input):
    print("Valid email address")
else:
    print("Invalid email address")
