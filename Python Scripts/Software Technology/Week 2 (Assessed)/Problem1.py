"""
Input a list of integers, print True if 6 appears as
either the first or last element in the list. The list will be length 1 or more.

// Sample I/O //
Input: 1 2 6
Output: True

Input: 1 2 3
Output: False

Input: 3 2 1
Output: False
"""

# Input a list of nums, map them as ints to input_list and split them.
input_list = list(map(int, input("Input a list of numbers: ").split()))
print(input_list)


def find_true(x):
    for i in range(len(x)):  # check if first or last element in input_list and return true.
        if x[0] == 6 or x[-1] == 6:
            return True
    else:
        return False


print(find_true(input_list))
