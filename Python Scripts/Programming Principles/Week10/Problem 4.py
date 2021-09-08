"""
// Counting Problem //
Problem: The Unix tool wc counts the numbers of characters, words and lines in a file.
Write your own version of wc that prompts for the name of the file to read, then prints
the counts. Assume a word may contain letters, digits, symbols and their mixture, but not
space. Hyphenated words, e.g. large-scale, shall be considered as one word.
"""

file_name = input("File name: ")
line_count = 0
word_count = 0
char_count = 0

with open(file_name) as f:  # Open the text file
    line = f.readline()  # Read a line from the file
    while line:
        words = line.split()  # Now split the line into words
        char_count += len(line)
        word_count += len(words)
        line_count += 1
        line = f.readline()

print("Characters: ", char_count)
print("Words: ", word_count)
print("Lines: ", line_count)
