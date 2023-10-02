from pathlib import Path

file = Path("learning_python.txt") # creates object from file

file_read = file.read_text() # reads entire file as 1 string

file_lines = file_read.splitlines() # reads file lines into a list

print(file_read)
    
for line in file_lines:
    print(line)

java_better = file_read.replace("Python", "Java")

print(java_better)

for line in file_read.splitlines():
    print(line)