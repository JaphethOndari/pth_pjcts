import re

def extract_phone_numbers(text):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    return re.findall(pattern, text)

text = "You can reach me at 123-456-7890 or 987-654-3210"
phone_numbers = extract_phone_numbers(text)
print("Phone numbers found:")
for phone_number in phone_numbers:
    print(phone_number)
