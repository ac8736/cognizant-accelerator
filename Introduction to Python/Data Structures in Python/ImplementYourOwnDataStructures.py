inventory = {}
print("Welcome to the Inventory Manager!")
while True:
    print("This is your current inventory.")
    for key, value in inventory.items():                                # print the current inventory
        print(f"Item: {key}, Quantity: {value[0]}, Price: {value[1]}")  
    print("What would you like to do?")                                 # offer the users the choices
    print("1. Add an item", end=" | ")
    print("2. Remove an item", end=" | ")
    print("3. Update an item", end=" | ")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":                                                   # add an item choice
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        inventory[item] = (quantity, price)
        print("Item added to the inventory.")
    elif choice == "2":                                                 # remove an item choice
        item = input("Enter the item name: ")
        if item in inventory:
            del inventory[item]
            print("Item removed from the inventory.")
        else:
            print("Item not found in the inventory.")
    elif choice == "3":                                                 # update an item choice
        item = input("Enter the item name: ")
        if item in inventory:
            quantity = int(input("Enter the new quantity: "))
            price = float(input("Enter the new price: "))
            inventory[item] = (quantity, price)
            print("Item updated in the inventory.")
        else:
            print("Item not found in the inventory.")
    elif choice == "4":                                                 # exit choice
        break
    else:
        print("Invalid choice. Please try again.")
    print()

total = 0
for key, value in inventory.items():
    total += value[0] * value[1]
print(f"Thank you for using the Inventory Manager! The total value of your inventory is: ${total}.")
