"""
// String Problem //
Write a program that reads strings (without digits or symbols in the string) typed by the user until an empty string
is entered. For each string, convert all words to lowercase, then sort and print the words into descending order
lexicographically.
"""

usrinp = input("Enter string: ")

while usrinp != "":
    ul = usrinp.lower()
    us = ul.split()
    us.sort(reverse=True)
    print("Output: ", end="")

    for i in us:
        lexi = ""
        lexi += i
        print(lexi, end=" ")
    s = input("\nEnter string: ")
