"""
Python : Programming Language : Easy to use, Versatile, High Level
Started at 1991
Installation : python.org
Portable
Code Editor ---- Source file ----- Python Interpreter[Compiler Byte Size code  ]

Install Python : Add .exe to path

Use vscode as a code editor

Syntax : print("Hello World")

Module : It is a file containing code written by someone else
PIP : Python package manager used to install modules

Built in Modules 

REPL : Read evaluate print loop

Comment : Single line comment : ctrl + forward /

"""
# 1. Write a program to print Twinkle twinkle little star poem in python.
# 2. Use REPL and print the table of 5 using it.
# 3. Install an external module and use it to perform an operation of your interest.
# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.
# 5. Label the program written in problem 4 with comments. 

import pyjokes

print(pyjokes.get_joke())

# 1. Write a program to print Twinkle twinkle little star poem in python.

print ("""SONG LYRICS
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
""")

# 2. Use REPL and print the table of 5 using it.

# Done using cmd

# 3. Install an external module and use it to perform an operation of your interest.

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

#4  Write a python program to print the contents of a directory using the os module.

import os

directory_path = "D:\DhyanlingaCosecrationDay2024\CWH_Python_Practice_02_07_2024" # Replace with the actual path

try:
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: Directory not found '{directory_path}'")

# 5. Label the program written in problem 4 with comments. 

import os

# Specify the directory path
directory_path = "/path/to/your/directory"  

# Get the list of all files and directories in the specified directory
contents = os.listdir(directory_path)  

# Print the contents
for item in contents:
    print(item)