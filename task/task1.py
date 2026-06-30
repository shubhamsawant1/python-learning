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