print("=" * 60)
# EXERCISE 4: Advanced Dictionaries (15 min)
print("=" * 60) 

print("\n--- EXERCISE 4: Dictionary Operaction ---\n ")

# Task 4.1: Dictionary methods 
print("Task 4.1: Dictionary Methods")
student = {"name": "siraj", "age": 21, "grade": "A", "gpa": 4.9}
print(f"Original: {student}")


# Get a value with default if not found
gpa = student.get("gpa", 3.8) # Returns 3.8 if gpa does't exits
print(f"GPA (with default): {gpa}")

# Add new key-value pair
student["email"] = "alice@gmail.com"
print(f"After adding email: {student}")

# Get all keys
keys = student.keys()
print(f"All values: {list[keys]}")

# Get all values
values = student.values()
print(f"All VAlues: {list[values]}")


# Get all keys
keys = student.keys()
print(f"All values: {list[keys]}")

# Get all values
values = student.values()
print(f"All VAlues: {list[values]}")

# Task 4.2: Updateing dictionaries
print("\nTask 4.2: Update Method") 
student.update({"age": 22, "grade": "A+"})
print(f"After Update: {student}")

# Task 4.3: Deleting from dictionary
print("\nTask 4.3: Deleting items")
if "email" in student:
   del student["email"]
print(f"After deleting email: {student}")

# Task 4.4: Nested dictionaries (dict inside dict)
print("\nTask 4.4: Nested dictionaries")
team = {
   "player1": {"name": "alice", "score": 85},
   "player2": {"name": "siraj", "score": 95},
   "player3": {"name": "simaran", "score":45},
   "player4": {"name": "viraj", "score": 88}
}

print(f"Team: {team}")

# Access nested value
alice_score = team["player1"]["score"]
print(f"Alice's score: {alice_score}")

for player in team:
   print(f"{team[player]}") # comprehensive dataset


# Task 4.5: List of dictionaries (very common)
print("\nTask 4.5: List of dictionaries")
students = [
   {"name": "Alice", "age": 21, "grade": "A"},
   {"name": "bob", "age": 22, "grade": "B"},
   {"name": "Carol", "age": 26, "grade": "C"}
]

# Loop and access 
print("Student and their grades:")
for student in students:
   print(f"    {student['name']}: {student['grade']}")

# Find specific student
search_name = str(input("Enter student name: "))
for student in students:
   if student['name'] == search_name:
      print(f" Found {search_name}: age {student['age']}")

print("\nCHECKPOINT: Can you work with nested dictionaries?")