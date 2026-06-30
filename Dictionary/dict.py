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