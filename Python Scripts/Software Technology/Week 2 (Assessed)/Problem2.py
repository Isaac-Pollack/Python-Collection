"""
Say that a "clump" in a list is a series of 2 or more
adjacent elements of the same value. Print the number of clumps in the given list.

// Sample I/O //
Input: 1 2 2 3 4 4
Output: 2
Input: 1 1 2 1 1
Output: 2
Input: 1 1 1 1 1
Output: 1
"""

# Input a list of nums, map them as ints to inputlist and split them.
inputlist = list(map(int, input("Input a list of numbers: ").split()))


def clumpfinder(x):  # Input list is x
    clumps = 0
    hit = 0  # Have we hit the 'clump'?
    for i in range(len(x) - 1):  # Start at 1st, stop at second last so we dont error out, cant have -1 inside brackets.
        if x[i] == x[i + 1] and hit == 0:
            hit += 1
            clumps += 1
        elif x[i] != x[i + 1]:  # Reset Hit if it is end of clump, so start new if hit == 0
            hit = 0
    return print(clumps)


clumpfinder(inputlist)
