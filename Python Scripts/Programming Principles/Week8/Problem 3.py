"""
// Arithmetic Progression Problem //
Write a function that given a list of numbers, returns True if and only if all of the
numbers in the list form an arithmetic progression, that is the difference between any two
successive numbers in the list is the same. Your main program should read a file containing
space-separated numbers as test lists, print each list and the outcome after calling the function.
"""


def checkIsAP(arr, n):
    if n == 1:
        return True

    arr.sort()
    d = arr[1] - arr[0]
    for i in range(2, n):
        if arr[i] - arr[i - 1] != d:
            return False
        return True


file = input()
f = open(file, "r")

arr = x = [int(x) for x in f.read().split()]  # I failed to get my split working properly due to time, this is messy.
n = len(arr)

print(*arr, checkIsAP(arr, n))
f.close()  # Close file
