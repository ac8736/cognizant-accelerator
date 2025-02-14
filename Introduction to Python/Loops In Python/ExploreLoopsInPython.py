# Task 1
num = int(input("Enter a number: "))
while num > 0:
    print(num, end=" ")
    num -= 1
print("Blast off! 🚀")

# Task 2
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}", end=" ")
print()

# Task 3
num = int(input("Enter a number: "))
prod = 1
for i in range(num, 0, -1):
    prod *= i
print(f"Factorial of {num} is {prod}")
