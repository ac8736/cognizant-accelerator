# Task 1
string = "Python is amazing!"
firstSixChars = string[:6]
anazing = string[10:16]
reverse = string[::-1]
print("First word:", firstSixChars)
print("Amazing part:", anazing)
print("Reversed string:", reverse)

# Task 2
string = " hello, python world! "
string = string.strip()
print(string)
print(string.capitalize())
string = string.replace("world", "universe")
print(string)
print(string.upper())

# Task 3
string = input("Enter a word: ")
reverse = string[::-1]
if string == reverse:
    print(f"Yes, {string} is a palindrome.")
else:
    print(f"No, {string} is not a palindrome.")
