def are_anagrams(str1, str2):
    return sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", ""))

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The given strings are anagrams of each other.")
else:
    print("The given strings are not anagrams of each other.")
