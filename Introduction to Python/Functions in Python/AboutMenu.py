# recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    # display the menu
    print("1. Calculate the factorial of a number.")
    print("2. Find the nth Fibonacci number.")
    print("3. Exit.")
    # get the user's choice
    choice = input("Enter your choice: ")

    # check if the choice is a number
    if choice.isdigit() == False:
        print("Please enter a number from the menu.")
        continue
    if choice == "1":   # calculate the factorial of a number if the user chooses option 1
        number = int(input("Enter the number to calculate its factorial: "))
        print(f"The factorial of {number} is {factorial(number)}.")
    elif choice == "2": # find the nth Fibonacci number if the user chooses option 2
        number = int(input("Enter the value of n to find the nth Fibonacci number: "))
        print(f"The {number}th Fibonacci number is {fibonacci(number)}.")
    elif choice == "3": # exit the program if the user chooses option 3
        break
    else:
        print("Invalid choice. Please try again.")
    print()
