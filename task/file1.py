# Safe file operations

print("\nTask: Working with files safely")
try:
  # try to open a file
  file = open("text.txt", "r")
  content = file.read()
  print(content)
  file.close()
except FileNotFoundError:
  print("File doesn't exit yet (that's OK)")