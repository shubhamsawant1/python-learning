# DAY 1 Python exercises 

print("=" * 50)
print("Welcome day1 python")
print("=" * 50)

print("n\--- EXERICISE 1: Print & Variables ---")

# Task 1.1 Print Your Name
# todo: Replace 'Your name ' With your actual name

name = "shubham sawant"

print("My name is" , name)

# create a variables and print them

age = 21
city = "Gokul shirgaon Kolhapur"

print(f"my name is {name} i am {age} years old I live in {city}")

# task 1.3: Do math with variables

x = 10
y = 5

sum_result = x + y
print(sum_result)

difference = x - y
print("Difference between Two numbers: ",difference)

product = x * y
print("1 chocalate is 10rs how much for 5 chocalate: ", product)

division = x / y

print("if 10 rs divided to 5 people how much per person: ", division)

# can you print your name and age

print("My name: ", name)
print("my age: ", age)

# EXERCISE 2: String (10 min)

print("=" * 50)

print ("n\ --- EXERCISE 2: String --- ")

# Task 2.1: String Operaction 
first_name = "shubham"
last_name = "sawant"

full_name = first_name + " " + last_name # joining string
print(f"Full name: {full_name}")

# task 2.2: String length

message = "Python is awesome!"
print(f"message: {message}")

print(f"Length: {len(message)} Charatesrs")

# Task 2.3: String uppercase / lowercase

text = "Hello WorLd"
print(f"Original: {text}")
print(f"uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# Task 2.4: String slicing (getting parts of strings)

word = "python"
print(f"First 3 letters: {word[0:3]}") # output : pyt
word_length = len(word)
print(f"Last 3 letters: {word[3:word_length]}") #hon
print(f"Reversed: {word[::-1]}") # nohtyp

# checkpoint: Can you combine two string and get their length?

print("=" * 50)

# EXERCISE 3: Lists (15 min)

print("n\ --- EXERCISE 3: Lists ---")

#Task 3.1 : Create and print a list

fruits = ["apple" , "mango" , "banana" , "orange" ]
print(f"Fruits: {fruits}")

# Task 3.2 Access list items (index starts at 0)

# apple
print(f"first fruits: {fruits[0]}")
print(f"second fruits: {fruits[1]}")
print(f"Third fruits: {fruits[2]}")
print(f"Fourth fruits: {fruits[3]}")

# Task 3.3 Add items to list 
fruits.append("grapes")
print(f"after adding grapes: {fruits}")

# Task 3.4 Remove items from list

fruits.remove("orange")
print(f"after removing grapes: {fruits}")

#task 3.5 Length of List
print(f"Length of fruits: {len(fruits)}")

# Task 3.6: Loop Througth List
print("\n Looping through fruits:")
# enumerate() 
for i, fruit in enumerate(fruits , start=1):
   print(f" {i}-{fruit}")

# Task 3.7: List of Numbers

numbers = [1 , 2 , 3 , 4 , 5]
print(f"\nNumbers: {numbers}")
print(f"sum: {sum(numbers)}")
print(f"max: {max(numbers)}")
print(f"min: {min(numbers)}")

# EXERCISE 4: Dictionaries (15 min)  
print("=" * 50)

print("\n--- EXERCISE 4: Dictonaries ---")

# Task 4.1: Create a Dictionaries(key - Value pairs)

person = {
   "name":"shubham",
   "age":21,
   "city":"kolhapur",
   "job":"Youtuber"
}

print(f"person: {person}")

# Task 4.2: Access dictionary values
print(f"Name: {person['name']}")
print(f"Age: {person["age"]}")
print(f"City: {person["city"]}")
print(f"Job: {person["job"]}")

# Task 4.3: Add new key-values pair

person['hobby'] = "coding"
print(f"After adding hobby: {person}")

# Task 4.4: Loop Through dictionary
print("\nLooping through person: ")
for key, value in person.items():
   print(f" {key} : {value}")

# Task 4.5: Multiple dictionaries in a List

students = [
   {"name": "shubham", "score": 85},
   {"name": "sahil", "score":90},
   {"name": "sidharth" , "score":78 }
]

print("\nStudents:")
for student in students:
   print(f" {student['name']}: {student['score']}")

   # Can you create a dictionary and access its values?
studentse = [
      {"studentName": "sahil", "score": 88},
      {"studentName": "virag" , "score":85}
   ]

for studente in studentse:
      print(f" value:{studente["score"]}")

print("=" * 50)

print("\n--- EXERCISE 5: If/Else Statement ---")

# Task 5.1: Simple if statement 
age = 20
if age >= 18:
   print(f"Age {age}: You are a adult")
else: 
    print(f"Age {age}: You are a minor")

# Task 5.2: If/elif/else

score = 85

if score >=95:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 55:
    grade = "C"
else:
    grade = "F"

print(f"Score {score}: Grade {grade}")

# Task 5.3: Multiple conditions (and ,or)

temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
    print("Perfect weather! Go outside!")
else: 
    print("Not ideal weather")

# Task 5.4: Cheacking if item is in list

favorite_colors = ["blue" , "green" , "red"]
my_color = "red"
if my_color in favorite_colors:
    print(f"{my_color} is one of my favorite colors!")
else:
    print(f"{my_color} is not in my favorites")
  

# can you write an if and else statement?

print("=" * 50)

# EXERCISE 6: Function (20 min)

print("\n--- EXERCISE 6: Functions ")

# Task 6.1: Simple Function 

def greet(name):
    """ This function greets someone"""
    message = f"hello, {name}! "
    return message

result = greet("shubham")
print(result)


# Task 6.2: Function with multiple parameters

def add(x , y):
    """ Add Two Numbers"""
    return x + y

sumofnumber = add(5 , 6)
print(f"5 + 6: {sumofnumber}")

#Task 6.3: Function that returns multiple values

def get_person_info():
    """ Return person informaction"""
    name = "shubham"
    age = 21
    city = "Kolhapur"
    return name , age, city

name ,age , city = get_person_info()

print(f"Name: {name}, Age: {age}, City: {city}")

# Task 6.4: Function with default values

def introduce(name , job="Engineer"): # Default Value
    """ Introduce someone with their job"""

    return f"{name} is a {job}"

print(introduce("shubham"))
print(introduce("shubham" , "gamer"))

# Task 6.5: Function that processes a list 

def get_average(numbers):
     """ Calculate average of numbers"""
     if len(numbers) == 0:
         return 0
     total = sum(numbers)
     average = total / len(numbers)
     return average

scoress = [30, 40 ,80 ,90 ,80]
avg = get_average(scoress)
print(f"Average score: {avg}")

# Checkpoint : can you  write a function  and call it 

# def addlist(lists, add):
    
#     lists.append(add)
#     return lists

# finallist = []

# for i in range(5):
#     # number = int(input("Enter a number: "))
#     addlist(finallist,number)

# print(finallist)

# print(" \n --- EXERICISE 7: Loops ---")

# Task 7.1: For Loop with range

print("Couning 1 to 5: ")

for i in range(1, 6): # 1 to 5 not including 6
    print(i)

# Task 7.2: For loop through list


print("\nSquaring Numbers: ")

for num in [1,2,3,4,5]:
    squared = num ** 2
    print(f"   {num} = {squared}")


# Task 7.3: While loop 
print("\nCounting Down: ")

count = 5
while count > 0:
    print(f"    {count}")
    count = count - 1
print("       Blassof!")


# loop With condotions

print("\nPrint even numbers 1-10: ")
for i in range(1,11):
    if i % 2 == 0: # divisible by 2
        print(f"      {i}")

# Task 7.5: Loop and build list

print("\nCreate list of square: ")

squares = []

for i in range(1,6):
    squares.append(i ** 2)
print(f"   {squares}")

# Checkpoint if you write a loop print something 5 times

names = []

for i in range(1,6):
    name = input("Enter names: ")
    names.append(name)
  
print(f" names: {names}")

# Mini challange (10 min)

print("\n--- EXERCISE 8: Mini Challange ----")

print("build a simple grade calculator! \n")

def calculator_grade(score):
    """ Convert Score in Grade"""

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 35:
        return "E"
    else:
        return "Fail"
    

# your_score = int(input("Enter your score: "))
# your_grade = calculator_grade(your_score)
# print(f"Your Grade: {your_grade}")

# Test With multiple Student

student_scores = [
    {"name":"shubham" , "score":95},
    {"name":"sahil", "score":98},
    {"name":"viraj", "score":35},
    {"name":"Parth", "score":65}
]

print("Students Grades: ")

for student in student_scores:
    name = student["name"]
    score = student["score"]
    grade = calculator_grade(score)
    print(f"    {name}: {score} points -> Grade {grade}")

    # success! You Complete Day 1!

    print("=" * 50)

    #FINAL CHALLENGE (Optional - 15 min)
    print("=" * 50)

    print("\n" + "=" * 50)
    print ("OPTIONAL FINAL CHALLENGE")
    print("=" * 50)

    print("\nTask: Create a simple contact book")
    print("Instructions:")
    print("1. Create a list of dictionaries (contacts)")
    print("2. Each contact has: name, phone, email")
    print("3. Loop through and print all contacts ")
    print("4. Try to find a contact by name")

    # Example Structure

    contacts = [

        {"name": "shubham", "phone": 8855-4564, "email": "smsepic10100@gmail.com"},
        {"name": "sidharth", "phone": 8855-5485, "email": "nirag0100@gmail.com"},
        {"name": "siara", "phone": 8855-6598, "email": "simaranc10100@gmail.com"},
        {"name": "simaran", "phone": 8855-1462, "email": "surajsira@gmail.com"},
        {"name": "suraj", "phone": 8855-4897, "email": "smserent@gmail.com"},
        {"name": "virag", "phone": 4568-6621, "email": "sirahyt@gmail.com"},
       

    ]

print("\nAll contacts: ")

for contact in contacts:
    print(f"     {contact["name"]}  {contact["phone"]} {contact["email"]}")

# search for a contact

search_name = str(input("Enter a name: "))
found = False
for contact in contacts:
    if contact["name"] == search_name:
        print(f"\nFound: {search_name}")
        print(f"  Phone: {contact['phone']}")
        print(f"  email: {contact["email"]}")
        Found = True
        break

if not found:
    print(f"\n{search_name} not found in contacts")

print("\n" + "=" * 50)
print("Congratulations! You Completed Day 1!")
print("=" * 50)
print("\nNext steps:")


