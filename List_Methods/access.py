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

fruits.remove("orange") #remove by name
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
item_to_check = str(input("Enter What you want to check: "))

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