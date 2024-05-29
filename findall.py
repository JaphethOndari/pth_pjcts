import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

text = "Please contact me at john@example.com or jane.doe@example.co.uk"
emails = extract_emails(text)
print("Email addresses found:")
for email in emails:
    print(email)
