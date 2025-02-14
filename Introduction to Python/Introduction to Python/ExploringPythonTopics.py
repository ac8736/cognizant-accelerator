# Task 1
name = "John"
age = 25
height = 6.2
print(f"Hey! My name is {name}. I am {age} years old and {height} feet tall.")

# Task 2
num1 = 10
num2 = 3
print("The sum of 10 and 3 is", num1 + num2)                # adding the numbers and printing the result
print("The difference between 10 and 3 is", num1 - num2)    # subtracting the numbers and printing the result
print("The product of 10 and 3 is", num1 * num2)            # multiplying the numbers and printing the result
print("The quotient of 10 and 3 is", num1 / num2)           # dividing the numbers and printing the result 

# Task 3
num = int(input("Enter a number: "))                        # taking input from the user
if num < 0:
    print("This number is negative. Better luck next time!")
elif num > 0:
    print("This number is positive. Awesome!")
else:
    print("Zero it is. A perfect balance!")
