import re

pattern = "[Pp]ython"
text = "I write code in python and Python!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))

# removes the spaces between

pattern = "\s"
text = "I like Python and it is amazing!"
split_text = re.split(pattern, text)
print("Split text:", split_text)

#text replacement

pattern = "Python"
replacement = "Java"
text = "Python is fun"
substituted_text = re.sub(pattern, replacement, text)
print("Substituted text:", substituted_text)