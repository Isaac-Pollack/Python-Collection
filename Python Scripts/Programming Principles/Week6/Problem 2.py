"""
// String Problem //
Write a program that allows the user to enter two lists of integers, calculate the sum of the first and last integers
in each list, and print the larger sum. In the event of a tie, print Same. When there is only one integer in the list
the sum is the integer itself.
"""

# INPUTS
i1 = input("List 1: ")
i2 = input("List 2: ")

# SPLIT BY WHITESPACE
l1 = i1.split(" ")
l2 = i2.split(" ")

# SUM = First Index
s1 = int(l1[0])
s2 = int(l2[0])

# If length of the list is > 1, add last index
if len(l1) > 1:
    s1 = s1 + int(l1[-1])
if len(l2) > 1:
    s2 = s2 + int(l2[-1])

# COMPARISONS
if s1 > s2:
    print(s1)
elif s1 < s2:
    print(s2)

# PRINTING "SAME"
else:
    print("Same")
