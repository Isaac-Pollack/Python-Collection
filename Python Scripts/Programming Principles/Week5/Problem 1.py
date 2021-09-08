"""
// 'A' String Problem //
Write a program that prompts for and reads strings until a string starts with "A" is entered,
then prints the shortest string that was entered. The output must match the punctuation.
"""

pString = []
check = False

while check is False:  #
    cString = str(input("Enter a string: "))
    pString.append(cString)

    for i in pString:
        if i.startswith('A'):  # If any of the list values in pString start with 'A' then do below
            print("Shortest was: ", min(pString, key=len))  # Prints shortest string using a 'key' of len(). VERY COOL.
            check = True
