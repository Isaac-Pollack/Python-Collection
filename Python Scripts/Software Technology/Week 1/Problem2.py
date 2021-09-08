"""
Write a Python program that prompt to read a cost of an item (less than or
equal to one dollar), gives the number of 50 cent, 20 cent, 10 cent, 5 cent and 1 cent
coins the buyer would receive if they handed over one dollar. You must minimise the
number of coins in the change.
"""

change = int(input('Please enter the cost of the item in cents ($1 is 100): '))

fiftys = change // 50
change -= fiftys * 50

twentys = change // 20
change -= twentys * 20

tens = change // 10
change -= tens * 10

fives = change // 5
change -= fives * 5

ones = change // 1
change -= ones * 1

print('Fiftys:', fiftys, '\nTwentys:', twentys, '\nTens: ', tens, '\nFives: ', fives, '\nOnes: ', ones)
