import re 

pattern = r"^(07|\+254|011)\d{8}$"  
number = input("Enter phone number: ")

match = re.match(pattern, number)
if match:
    print("Valid phone number.")
else:
    print("Invalid phone number.")
