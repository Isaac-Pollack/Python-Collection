"""
Write a program that prompt to read a time interval in hours, minutes and seconds
and prints the equivalent time in just seconds.

// Sample I/O //
Input: 1 10 20
Output: 4220
Input: 0 40 50
Output: 2450
"""

h, m, s = map(int, input("Input: ").split())  # We need to have int values not strings, map it.
print(h * 3600 + m * 60 + s)  # * by how many seconds in those values and print it
