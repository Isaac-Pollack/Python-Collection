"""
// String Problem //
We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.
write a function to print True if all the g's in the given string are happy, otherwise print False.
"""

def happy_function(stri):
    for i in range(len(stri) - 1):
        if stri[i] == 'g' and stri[i + 1] == 'g':  # Condition for whether adjacent characters are g's or not
            return True  # If satisfied return True
    return False  # if no adjacent g's return false


String = "xggt"  # STR 1
print("String:", String)  # Print the string as per problem
print("Happy?:", happy_function(String))  # Call the happy check method

String1 = "abgsx"  # STR 2
print("String:", String1)
print("Happy?:", happy_function(String1))

String2 = "g"  # STR 3
print("String:", String2)
print("Happy?:", happy_function(String2))

String3 = "brggsomr"  # STR 4
print("String:", String3)
print("Happy?:", happy_function(String3))
