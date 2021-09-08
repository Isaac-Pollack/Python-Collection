"""
// Integer sorting //
Sort 3 input integers in descending order without using list or sort()
"""

# Inputs
int1 = int(input('What is Integer 1? '))
int2 = int(input('What is Integer 2? '))
int3 = int(input('What is Integer 3? '))

if int1 > int2 and int1 > int3:
    if int2 > int3:
        print("SORTED:", int1, int2, int3)
    else:
        print("SORTED:", int1, int3, int2)

elif int2 > int1 and int2 > int3:
    if int1 > int3:
        print("SORTED:", int2, int1, int3)
    else:
        print("SORTED:", int2, int3, int1)

else:
    if int1 > int2:
        print("SORTED:", int3, int1, int2)
    else:
        print("SORTED:", int3, int2, int1)