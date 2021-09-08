"""
// String Problem //
Problem: Write a program that prompts for the names of a source file to read and a target
file to write, and copy the content of the source file to the target file, but get all empty lines
removed, then output the number of empty lines removed.
"""

# taking input of src and dest file names
src_file = input("Source file name: ")
dest_file = input("Target file name: ")

fr = open(src_file, "r")
text = fr.read()
l_lines = text.split("\n")  # Split by new lines if more than empty stings

if len(l_lines[-1]) == 0:
    l_lines.pop()

count = 0
fw = open(dest_file, "w")

for i in l_lines:  # Discard lines with len 0, as they are empty
    if len(i) == 0:
        count = count + 1
    else:
        fw.write(i + "\n")
print("lines removed: ", count)
fw.close()
