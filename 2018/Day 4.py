"""
Ishaan Patel
12/20/2018
Advent Of Code - Day 4
"""

import re
from statistics import mode

def sleep(fileName):
    """ Part 1: Returns Id of chosen guard multiplied
    by the minute chosen """

    lst = open(fileName, 'r').readlines()
    temp = {}
    c = gap = start = end = val = g = 0
    awake = True
    guard = -1
    times = []
    merge = []
    min = []

    for x in lst:
        temp[c] = re.findall(r"\d+", x)
        for n in range(len(temp[c])):
            temp[c][n] = int(temp[c][n])
        c += 1

    d = (sorted(temp.items(), key = lambda x: x[1]))
   
    for x in d:
        if len(x[1]) == 6:
            if gap != 0:
                times+= [[guard, gap]]
            guard = x[1][5]
            gap = 0
            start = end = 0
            awake = True
        elif awake:
            awake = False
            start = x[1][4]
        elif not awake:
            awake = True
            end = x[1][4]
            gap += (end - start)

    times.sort()

    for x in range(1, len(times)-1):
        if x == 1:
            val = times[x][1]
        if times[x][0] == times[x-1][0]:
            g = times[x][0]
            val += times[x][1]
        elif times[x][0] != times[x-1][0]:
            merge.append([g, val])
            g = times[x][0]
            val = times[x][1]

    merge.sort(key = lambda x: x[1])

    chosen = merge[-1][0]
    for x in range(0,60):
        min.append([x, 0])

    for x in d:
        if len(x[1]) == 6:
            guard = x[1][5]
            awake = True
        elif awake and guard == chosen:
            awake = False
            start = x[1][4]
        elif not awake and guard == chosen:
            awake = True
            end = x[1][4]
            for i in range(start, end):
                min[i][1]+= 1
            start = 0
            end = 0

    min.sort(key = lambda x:x[1])
    minute = min[-1][0]

    """ Part 2 """
    freq = []
    for x in range(0,60):
        freq.append([x, []])
    for x in d:
        if len(x[1]) == 6:
            guard = x[1][5]
            awake = True
        elif awake:
            awake = False
            start = x[1][4]
        elif not awake:
            awake = True
            end = x[1][4]
            for i in range(start, end):
                freq[i][1] += [guard]
            start = 0
            end = 0

    max = []
    for x in freq:
        c = 0
        try:
            m = mode(x[1])
        except:
            m = 0
        for y in x[1]:
            if m == y:
                c+= 1
        max.append([x[0], m, c])

    max.sort(key = lambda x: x[2])
    val = max[-1][1] * max[-1][0]

    return chosen * minute, val

print(sleep("day4_input.txt"))

