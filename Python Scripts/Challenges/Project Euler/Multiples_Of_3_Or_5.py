"""
Multiples of 3 or 5: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Valuable Takeaways:
- Sets are unique, so instead of iterating the two lists, just cast as a set and it does it for you.
- It seems better to design input validation outside of the func, so it is more modular.
"""
import sys


# List numbers below (input)
def multiples_below(x):
    m3 = []
    m5 = []
    both = []
    for i in range(3, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            both.append(i)
        elif i % 3 == 0:
            m3.append(i)
        elif i % 5 == 0:
            m5.append(i)

    # Show the multiples of 3, 5 and both of them.
    print(f"\nMultiples of 3 are: {m3}")
    print(f"Multiples of 5 are: {m5}")
    print(f"Multiples of both are: {both}\n")

    # Combine lists
    combined = set(m3 + m5)
    # Sum them all
    answer = sum(combined) + sum(both)

    # Escape Codes: \u001b[32m for green, \n\033[1m for Bold, \033[94m for blue.
    # Providing slightly better visualisation.
    print(f"The sum of all multiples of 3 and 5 under \u001b[32m{x}\u001b[0m is: \n\033[1m\033[94m{answer}")


# Run statement
num = None
while num is None:
    try:
        # try and convert the string input to a number
        num = int(input("What number would you like to find multiples of 3 & 5 of up-to?:\n"))
        if num < 3:
            print("Your number cannot be less than 3.")
            sys.exit()
    except ValueError:
        # Get mad if not integer
        print("'{input}' is not an integer, please enter an integer only.\n".format(input=num))

multiples_below(num)
