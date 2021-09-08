"""
Write code that reads two integers from the keyboard. If the first
integer is in the range 1. . 100 and the first integer is less than the second integer OR if
the first integer is at least twice the second integer and the second integer is not in the
range -8..16 (with the exception it can be zero) print True. Otherwise print False. You
must NOT use the Python if or if-else statement. All ranges are inclusive.
"""

firstInt = (int(input("First Integer: ")))
secondInt = (int(input("Second Integer: ")))

print(firstInt in range(1, 100) and firstInt < secondInt or firstInt >= secondInt and secondInt not in range(-8, 16)
      or secondInt == 0)
