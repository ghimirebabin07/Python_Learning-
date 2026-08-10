from pathlib import Path

file = Path("hello.txt")

file.write_text("Hello, I am learning Python!")

print(file.read_text()) 