"""
// Indefinite Loop Problem //
Input integers until 0 is entered, then count how many numbers were positive.
"""

# Declarations
positive_nums = 0
count = None
user_input = int(input('Enter a number: '))  # For readability.

# Loop Logic
while count != 0:
    count = user_input
    if count > 0:
        positive_nums += 1
    elif count < 0:  # Essentially, do nothing but ask for another number.
        count = user_input
    else:  # If count = 0, then do this and break.
        print(positive_nums, 'positive numbers were entered.')
