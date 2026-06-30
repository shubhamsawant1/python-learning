# DAY: PYTHON EXERCISES (Advanced Basics)

#Prerequisites: Completed Day 1 exercises

print("=" * 60)
print("DAY 2: ADVANCED BASIC")
print("Building on what learned Yesterady")
print("=" * 60)

# QUICK REVIEW: Day 1 Concepts (10 min)

print("\n--- QUICK REVIEW FROM DAY 1 ---\n")

# Review 1: variables and Strings

name = "Python Learner"
age = 21
print(f"Hellow {name}, You are {age} years old" )

#Review 2: Lists and loops  #join()
words = ["I" , "Love" , "You"]
hobbies = ["coding" , "reading" , "gaming"]
print(f"My hobbies: {', '.join(hobbies)}")
print(f"I want to say {' '.join(words)}")

# Review 3: Dictionaries 
person = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"Person: {person['name']} from {person['city']}")

# Review 4: Simple functino
def greet(name):
  return f"Welcom, {name}!"

name2 = str(input("Enter your name: "))
message = (greet("sidarth"))
print(message)

print("\nDAy 1 concepts review complete \n")

# EXERCISE 1: Working with User Input (15 min)

print("--- EXERCISE 1: User Input ---\n")
# Task 1.1: Get name from user 
print("Task 1.1: Enter your name: ")
user_name = input("What's your name?")
print(f"Nice to meet you {user_name}!")

#Task 1.2: Get age and calculate birth year
print("\nTask 1.2: Enter Your age:")
user_age = int(input("How old are you?"))
birth_year = 2026 - user_age
print(f"You were born around {birth_year}")

#Task 1.3: Get multiple inputs
print("\nTask 1.3: Tell me about yourself:")
favorite_color = input("Favorite color? ")
favorite_food = input("Favorite food?")
print(f"you like {favorite_color} and {favorite_food}")

# Task 1.4: simple calculation with user input
print("\nTask 1.4: Simple calculator:")
num1 = float(input("First number?"))
num2 = float(input("Second number?"))

result = num1 + num2

print(f" {num1} + {num2} = {result}")

print("\n CHECKPOINT: Can you get user input and do math with it")

#EXERCISE 2: Error Handling (20 min)

print("\n EXERCISE 2: ERROR HANDLING ---")

# Task 2.1: Try/Expect basic (preventing crashes)
print("Task 2.1: Safe number conversion")

try:
    user_input = input("Enter a number: ")
    number = int(user_input) # This can fail if not a number!
    print(f"You entered: {number}")
except ValueError: #Catches if conversion fails
   print("That's not valid number!")

# Task 2.2: Multiple except statements 
print("\nTask 2.2: Multiple erroe types")

try:
   numbers = [1,2,3]
   index = int(input("Enter index (0-2): "))
   value = numbers[index]
   print(f"Value at index {index}: {value}")
except ValueError:
   print("Please enter a valid number")
except IndexError:
   print("That index doesn't exits!")


# Task 2.3: Finally (runs no matter what)
print("\nFinally block")
try:
   num_1 = int(input("Enter number 1: "))
   num_2 = int(input("Enter number 2: "))
   result = num_1 / num_2
   print(f"Result: {result}")
except ZeroDivisionError:
   print("Can't divide by zero")
finally:
   print("(This always runs)")


# Task 2.4: Safe file operations 
print("\nTask 2.4: Working with files safely")

try:
   # Try to open a file
   file = open("test.txt", "r")
   content = file.read()
   file.close()
except FileNotFoundError:
   print("File doesn't exits yet (that's OK)")


print("\nCHECKPOINT: Do you understand try/except")
print("=" * 60)
# EXERCISE 3: Advanced Lists & List Methods (15 min)
print("=" * 60)
# Task 3.1: List Methods 
print('Task 3.1: List methos')
fruits = ['apple', 'banana', 'orange']
print(f"Original: {fruits}")

for fruit in fruits:
   print(f"  -{fruit}")

fruits.append("grape")
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")# Insert at position 1
print(f"After insert: {fruits}")

fruits.remove("Orange")
print(f"After remove {fruits}")

popped = fruits.pop() # remove and return last item
print(f"After pop (removed {popped}):{fruits}")

#Task 3.2: List sorting 
print("n\
      Task 3.2: Sorting")
numbers = [5,6,4,6,9,4]
print(f"Original: {numbers}")

sorted_numbers = sorted(numbers) #Returns new sorted list
print(f"Sorted (new list): {sorted_numbers}")

numbers.sort() #Sorts the list in place
print(f"After .sort(): {numbers}")

# Task 3.3: Reversing 
print("\nTask 3.3: Reversing")
words = ["hello", "world", "python"]
print(f"Original: {words}")
words.reverse()
print(f"Reversed: {words}")

# Task 3.4: Checking if item exits
print("\nTask 3.4: Membership testing")
shopping_list = ["milk", "eggs", "bread", "cheese"]
item_to_check = "eggs"

if item_to_check in shopping_list:
   print(f"{item_to_check} is in the list")
else:
   print(f"{item_to_check} is NOT in the list")

# Task 3.5: List comprehension (create lists quickly)
print("\nTask 3.5: List comprehension ")
# old way: 
squares = []
for i in range(1, 6):
   squares.append(i ** 2)
print(f" Squares (new way): {squares}")

# Filter even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
evens = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")

print("\nCHECKPOINT: Can you use list methods and comprehension?")

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

print(f"Team": {team})