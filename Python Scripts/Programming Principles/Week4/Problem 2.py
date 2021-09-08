"""
// Fibonacci Sequence //
Given an input of 'n', output the first 'n' Fibonacci Numbers, to at most 4 numbers max in a row.
"""

# Declarations
n = int(input('Enter a positive number: '))  # For readability.
num1, num2, ans = 0, 1, 0
count = 1

# Fib Logic
while count <= n:
    if count % 4 == 0:
        print(ans, end="\n")  # Print and then new line if divisible by 4
        count += 1
    else:
        print(ans, end=" ")
        count += 1  # Count = Count + 1

    num1 = num2  # Careful of indenting here, outside if/else.
    num2 = ans
    ans = num1 + num2

if n <= 0:
    print('Please input a positive number to return a sequence.')
