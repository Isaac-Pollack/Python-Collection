"""
// Carpet Calculation Problem //
Roll carpet comes in 3.66 meters wide. Carpet is paid for by the total number of whole meters that need to be cut
from the roll. It may be laid in a rectangular room length-ways or width-ways. Either way there might be some wastage.
Write a program that asks for the dimensions of the room until either dimension entered is 0 or less.
"""
from math import ceil

sortL = []
carpetWidth = 3.66

while True:
    dim1 = float(input("Enter room dimension 1? (m): "))
    dim2 = float(input("Enter room dimension 2? (m): "))

# Put it in a list, sort it and assign values
    sortL.append(dim1)
    sortL.append(dim2)
    length = max(sortL)
    width = min(sortL)

    print(format(dim1, '.3f'))  # String formatting to print max 3 spaces after the integer
    print(format(dim2, '.3f'))

    print("Total length required length-ways = ", ceil(width) / carpetWidth, "m")
    print("Total length required width-ways = ", width, "m")
