"""
Write a program that generates the Baum-Sweet sequence from 0 to n.
(Baum-Sweet Sequence: https://en.wikipedia.org/wiki/Baum%E2%80%93Sweet_sequence)

= Example = 
Input: '20'
1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0
"""


def baum_sweet(z):
    num_of_zeros = []
    count_of_zeros = []
    if z == "0":
        n = 1
    else:
        for b in val:
            if b == "0":
                num_of_zeros.append(b)
            else:
                count_of_zeros.append(num_of_zeros.count("0"))
                num_of_zeros = []
        count_of_zeros.append(num_of_zeros.count("0"))

        n = 1
        for b in count_of_zeros:
            if b % 2 == 1:
                n = 0
    return n


num = int(input("Length of Sequence: "))
baum_sweet_sequence = []

for i in range(num + 1):
    x = bin(i)
    val = x[2:]
    baum_sweet_sequence.append(baum_sweet(val))

print(", ".join(str(e) for e in baum_sweet_sequence))
