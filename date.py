import re

def validate_date(date):
    # Date format DD/MM/YYYY
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/((19|20)\d\d)$"
    if re.match(pattern, date):
        return True
    else:
        return False

date = input("Enter a date (DD/MM/YYYY): ")
if validate_date(date):
    print("Date format is valid.")
else:
    print("Date format is not valid.")
