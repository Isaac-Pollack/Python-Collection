"""
// Digits to Underline Problem //
Write a program that converts all digits in a string to underline.
"""

while True:  # Indefinite Loop for display purposes
    inputS = str(input("Input a string? "))
    j = '_'  # What we will replace numbers with

    for i in inputS:  # Loop i value
        if i.isdigit():
            inputS = inputS.replace(i, j)  # If i is a digit, replace it with j (Which we said = '_')

    print(inputS)
