# Task 1
def greet_user(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

greet_user("Alice")
print("The sum of 3 and 5:", add_numbers(3, 5))

# Task 2
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")
describe_pet("Bella")

# Task 3
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:", end=" ")
    for ingredient in ingredients:
        print(f"- {ingredient}", end=" ")
    print()
make_sandwich("lettuce", "tomato", "cucumber")

# Task 4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Factorial of 5:", factorial(5))
print("10th Fibonacci number:", fibonacci(10))
