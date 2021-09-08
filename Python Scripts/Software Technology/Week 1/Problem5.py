"""
Given three integers, a b c, one of them is small, one is medium and one is
large. Print True if the three values are evenly spaced, so the difference between small
and medium is the same as difference between medium and large. Otherwise, print
False.
"""

inputInts = sorted(list(map(int, input("Please provide 3 Integers: ").split())))


def evenlySpaced(x):
    if x[1] - x[0] == x[2] - x[1]:
        return True
    else:
        return False


print(evenlySpaced(inputInts))
