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
   result = 10 / 2
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