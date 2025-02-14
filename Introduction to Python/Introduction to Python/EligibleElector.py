age = input("How old are you? ")
if age.isdigit():   # checking if the input is a number
    age = int(age)
    if age >= 18:   # checking if the user is eligible to vote
        print("Congratulations! You are eligible to vote. Go make a difference!")
    else:           # if the user is not eligible to vote
        print(f"Oops! You’re not eligible yet. But hey, only {18 - age} more years to go!")
else:
    print("Oops! Looks like you entered something weird (negative or characters)! Please try again.")
