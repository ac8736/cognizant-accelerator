print("Welcome to the error handling calculator.")
while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice == 5:
            break
        if choice < 1 or choice > 5:
            print("Invalid input.")
            continue
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == 3:
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            try:
                print(f"{num1} / {num2} = {num1 / num2}")
            except ZeroDivisionError:
                print("Can't divide by zero.")
    except ValueError:
        print("Invalid input.")
