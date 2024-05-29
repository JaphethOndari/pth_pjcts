import re



text = "Hello Mr. Smith. How are you, Mr. Johnson?"
pattern = r"\bMr\.\b"  # Word boundary ensures it only matches whole words "Mr."
add_text = ""

replaced_text = (pattern, add_text, text)
print("Original text:", text)
print("Replaced text:", replaced_text)
