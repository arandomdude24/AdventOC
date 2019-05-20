"""
Ishaan Patel
12/22/2018
Advent Of Code - Day 6
"""

import re

def parse(fileName):
    """ Parse the data and puts it into a list """
    lst = open(fileName, 'r').readlines()
    val = []
    for x in lst:
        num = re.findall(r"\d+", x)
        val += [num]
    for x in range(len(val)):
        for y in range(len(val[x])):
            val[x][y] = int(val[x][y])
    return val

val = parse("day6_input.txt")

def grid(lst):
    """ Makes the grid and returns the max non infinite size"""
    g = []
    for x in range(400):
        row = []
        for y in range(400):
            row.append(-1)
        g.append(row)

    for a in range(len(lst)):
        x = lst[a][0]
        y = lst[a][1]
        g[x][y] = a

    def printer():
        for x in g:
            print(x)

    numList = []

    for x in range(len(g)):
        for y in range(len(g[x])):
            dist = []
            if g[x][y] == -1:
                for a in val:
                    dist += [abs(a[0] - x) + abs(a[1] - y)]
                    num = dist.index(min(dist))
                    if dist.count(min(dist)) != 1:
                        g[x][y] = -1
                    else:
                        g[x][y] = num
            if g[x][y] not in numList and g[x][y] != -1:
                numList += [g[x][y]]
    numList.sort()

    for y in g[0]:
        if y in numList:
            numList.remove(y)
    for y in g[-1]:
        if y in numList:
            numList.remove(y)
    for x in range(len(g)):
        if g[x][0] in numList:
            numList.remove(g[x][0])
        if g[x][-1] in numList:
            numList.remove(g[x][-1])

    values = []
    for n in numList:
        c = 0
        for x in g:
            for y in x:
                if y == n:
                    c+= 1
        values += [[n, c]]

    values.sort(key = lambda x : x[1])

    region = 0
    for x in range(len(g)):
        for y in range(len(g[x])):
            dist = []
            for a in val:
                dist += [abs(a[0] - x) + abs(a[1] - y)]
            if sum(dist) < 10000:
                region += 1

    return values[-1][1], region

print(grid(parse("day6_input.txt")))

