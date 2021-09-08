"""
// Diamond Generation //
Given 'n' print a diamond shape with 2*n-1 rows
"""

# Declarations
n = int(input("Enter a positive number: "))

if n <= 0:  # Error checking 0 or negative numbers.
    print("A positive number is required to draw a diamond.")

else:
    for i in range(1, n + 1):  # Start, Stop, Step.
        print((n - i) * " " + (i * " *"))  # = 5x whitespaces + i * " *"

    for i in range(n - 1, 0, -1):  # Starts at 1 less then the 'belt' of the diamond
        print((n - i) * " " + (i * " *"))
