from pathlib import Path

file = Path("hello.txt")

file.write_text("Hello, I am learning Python!")

print(file.read_text()) 

#program 2 

file = Path("hello.txt")

if file.exists():
    print("File exists")
else:
    print("File does not exist")