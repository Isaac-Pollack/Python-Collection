"""
Find and print all numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 2100
"""

for i in range(2000, 2100):  # Loop to check every number
    if i % 7 == 0 and i % 5 != 0:  # Our conditional statements to check if its OK to print
        print(i)
