"""
// Year to Year Problem //
Given starting and ending years, write a function to calculate the number of days from starting year to
ending year inclusive.
"""

year1 = int(input("Year 1? "))
year2 = int(input("Year 2? "))

# The sum of the range of year1 and year2+1 (This should be inclusive of year2)
# 366 days if leap year, 365 if not. Trying to use lists to append data here proved too troublesome.
# While ugly, it works. (Would love feedback on if there is a cleaner way to do this)
print(sum([366 if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0 else 365 for x in range(year1, year2+1)]))
