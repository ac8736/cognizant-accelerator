# Task 1
fruits = ["apple", "orange", "cherry", "date", "strawberry"]
print("Original list:", fruits)
fruits.append("banana")
print("After adding a fruit:", fruits)
fruits.remove("date")
print("After removing a fruit:", fruits)
fruits = fruits[::-1]
print("Reversed list:", fruits)

# Task 2
profile = {"name": "Andy", "age": 22, "city": "New York"}
profile.update([{"favorite_color", "blue"}])
profile["city"] = "San Francisco"
for key, value in profile.items():
    print(f"{key}: {value}")

# Task 3
favoriteThings = ("Iron Man", "Bohemian Rhapsody", "Percy Jackson")
print("Favorite things:", favoriteThings)
print("Length of the tuple:", len(favoriteThings))
