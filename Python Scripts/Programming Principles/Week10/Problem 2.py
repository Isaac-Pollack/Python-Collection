"""
// Name of File //
Problem: Write a program that prompts for the name of a file, then print the first two lines
and the last two lines of the file.
"""

# Open the file
file = open(input("File name: "))
print('Output:')
for i in range(2):  # Read 2 lines
    line = file.readline().strip()  # Read line adds a new line, so strip it
    print(line)

for j in (file.readlines()[-2:]):  # Read the last two
    print(j, end="")  # Strip it again, this time easier
