"""
Ishaan Patel
Advent Of Code - 2018 Day 2 V2
5/20/19
"""

import time

FILE = 'day2_input.txt'
lst = open(FILE, 'r').readlines()

def checksum():
    """
    Returns the checksum of the list
    Amount of ID's with a letter that repeats 2 times
    multiplied by number of Id's with a letter that repeats 3 times
    """

    double = triple = 0
    for x in lst:
        table = {}
        for i in x:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        if 3 in table.values():
            triple += 1
        if 2 in table.values():
            double += 1
    return double*triple

def similar():
    """
    :return: The common letters between the 2 ID's that only 
    have a difference of one letter
    """
    lst.sort()
    for x in lst:
        for y in lst:
            val = ''
            diff = 0
            for z in range(len(y)-1):
                if x[z] != y[z]:
                    diff += 1
                else:
                    val += y[z]
            if diff == 1:
                return val

start_time = time.time()
print(checksum())
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(similar())
print("--- %s seconds ---" % (time.time() - start_time))
