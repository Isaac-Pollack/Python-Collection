"""
// List Merge Problem //
Given two lists, write a function that merges these two lists in descending order.
Your main program will allow the user enter two lists of numbers and end input with a blank
line for list 1. You are not allowed to concatenate two lists into a new list and then call the
built-in sort() function to sort the new list in descending order. But it is allowed to sort
two lists in descending order before merge. Don’t worry about the complexity of the merging algorithm.
"""


def merge(list1, list2):
    new_list = []
    list1.sort(reverse=True)  # Sort them both
    list2.sort(reverse=True)

    size_1 = len(list1)  # Get the length
    size_2 = len(list2)

    i = 0
    j = 0

    while i < size_1 and j < size_2:  # if element of list1 > list2
        if list1[i] > list2[j]:
            new_list.append(list1[i])
            i += 1

        else:  # Otherwise, add element of list2 to end of new_list, appending
            new_list.append(list2[j])
            j += 1

    new_list = new_list + list1[i:] + list2[j:]  # Merge them both
    return new_list


while 1:
    my_list_1 = []
    my_list_2 = []

    x = input("List 1 : ")
    if x == "":
        break  # break out of the loop if value is null
    for item in x.split():  # loop to split value of x, and store it
        my_list_1.append(int(item))

    x = input("List 2 : ")  # We can utilize x for both lists here, and still have error checking
    for item in x.split():
        my_list_2.append(int(item))

    print(merge(my_list_1, my_list_2))  # Now call it with parameters
