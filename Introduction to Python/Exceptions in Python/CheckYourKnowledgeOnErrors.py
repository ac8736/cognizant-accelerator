# task 1
try:
    num = int(input("Enter a number: "))
    try:
        print(f"100 divided by {num} is {100 / num}")
    except ZeroDivisionError:
        print("Can't divide by zero.")
except ValueError:
    print("Invalid Input.")

# task 2
try: 
    lst = []
    print(lst[0])       # error attempting to access index 0 of an empty list
except IndexError:
    print("Index error. Index out of range.")
try:
    dic = {}
    print(dic['key'])   # error attempting to access a key that doesn't exist in the dictionary
except KeyError:
    print("Key error. Key not found in dictionary.")
try:
    "string" + 2        # error attempting to add a string and an integer
except TypeError:
    print("Type error. Can't add string and integer.")

# task 3
result = 0
try:
    firstNum = int(input("Enter the first number: "))
    secondNum = int(input("Enter the second number: "))
    result = firstNum / secondNum
# handle multiple exceptions
except ZeroDivisionError:
    print("Can't divide by zero.")
except ValueError:
    print("Invalid Input.")
else:
    print(f"The result is {result}.")
finally:
    print("This always executes.")
