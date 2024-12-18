import os
print(os.getcwd())  # Prints the current working directory

with open(r"C:\Users\pc\Desktop\codeX\codeX\1218\example.txt", "r") as file:
    content = file.read()
    print(content)

# Open a file in write mode
with open("example.txt", "w") as file:
    file.write("Hello, CodeX! This is a new line. \nToday we are moving on to File Handling.")
    print("File written successfully!")

# Open a file in append mode
with open("example.txt", "a") as file:
    file.write("\nThis is a new line appended to the file.")
    print("File appended successfully!")
    
# Open a file and read line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
