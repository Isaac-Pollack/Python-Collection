"""
// Marks - Pass/fail Calculator //
"""

# Input
marks = int(input('How many marks? '))

# Logic
if 85 <= marks <= 100:
    print(7)
elif 75 <= marks <= 84:
    print(6)
elif 60 <= marks <= 74:
    print(5)
elif 50 <= marks <= 59:
    print(4)
elif marks <= 49:
    print('F')

# Error Checking
elif marks < 0 or marks > 100:
    print('This is an incorrect input, please specify a number between 0 - 100')
