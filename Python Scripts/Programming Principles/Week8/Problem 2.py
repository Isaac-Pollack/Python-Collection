"""
// List Duplicates Problem //
Given two lists, write a function that takes these two lists as the input arguments
and returns the list of all the elements in the first list that occur in the second list.
The returned list shall not contain duplicate elements.
Your main program will allow the user enter two lists of numbers and end input with a blank line for list 1.
"""


def duplicates(list1, list2):
    dup = []
    for x in list1:
        if (not x in dup) and (x in list2):
            dup.append(x)
    return list(set(dup))


input1 = input("List 1: ")
while input1 != "":
    lst1 = [int(x) for x in input1.split(" ")]
    lst2 = [int(x) for x in input("List 2: ").split(" ")]
    print("Output:", duplicates(lst1, lst2))
    input1 = input("List 1: ")
