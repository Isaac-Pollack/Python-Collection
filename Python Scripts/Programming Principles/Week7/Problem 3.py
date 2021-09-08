"""
// Name-Average-Print Problem //
Problem: Write a program that prompts for the name of a file containing numbers in each
line, prints the average of each line. Assume each line contains numbers only and they are
separated by spaces.
"""

file = open(input("File name: "), 'r')  # Open File in read mode
lines = file.readlines()

for line in lines:  # Now average each line
    count = 0
    sum_number = 0
    for i in line.split(' '):
        count += 1
        sum_number += int(i)
    print(f"The average of line {count} is {sum_number / count}")  # Now print it all
