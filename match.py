import re

pattern = "python$"
text = "i love python"
match = re.search(pattern, text)
print("outcome is", bool(match))


pattern = "^hello"
text = "hello world"
match = re.search(pattern, text)
print("outcome is", bool(match))


pattern = "py?.n"
text = ["python coding, pyn "]
match = re.search(pattern, text)
print("outcome is", bool(match))

pattern= "py{1,2}n"
text = "i love pyn, pyyn, pyyyn"
match = re.search(pattern, text)
print("outcome is", bool(match))

