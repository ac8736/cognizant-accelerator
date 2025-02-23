password = input("Enter a password: ")

appropriateLength = len(password) >= 8

containsUppercase = False
containsLowercase = False
containsDigit = False
containsSpecialCharacter = False
for char in password:
    if char.isupper():
        containsUppercase = True
    elif char.islower():
        containsLowercase = True
    elif char.isdigit():
        containsDigit = True
    else:
        containsSpecialCharacter = True

if appropriateLength and containsUppercase and containsLowercase and containsDigit and containsSpecialCharacter:
    print("Your password is strong.")
if not appropriateLength:
    print("Your password is too short.")
if not containsUppercase:
    print("Your password does not contain an uppercase letter.")
if not containsLowercase:
    print("Your password does not contain a lowercase letter.")
if not containsDigit:
    print("Your password does not contain a digit.")
if not containsSpecialCharacter:
    print("Your password does not contain a special character.")
