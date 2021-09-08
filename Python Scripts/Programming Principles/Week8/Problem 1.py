"""
// List Spin Problem //
Write a function that given a list of numbers, rotate the numbers so
the first number becomes the last, and the rest of the numbers move one position forward.
Make the rotation iterative until it returns to the initial form.
"""

def spinlist(lis):
    print(lis)

    for i in range(len(lis)):  # Loop the length of the list
        count = lis[0]
        lis.remove(count)
        lis.append(count)  # Take it from the front and put it on the end
        print(lis)


# Our input list
list1 = [int(x) for x in input("Lists: ").split(" ")]  # Loop inside the input with split rather than a million lines
spinlist(list1)  # Run our function on the loop, with string formatting
