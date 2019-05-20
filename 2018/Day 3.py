'''
Ishaan Patel
Advent Of Code - 2018, Day 3
'''

import re

def overlap(fileName):
    """ Day 3 Part 1, finds out how many squares
     have overlapping claims """
    lst = open(fileName, 'r').readlines()
    val = {}
    c = 0
    maxW = 0
    maxH = 0
    num = 0

    for x in lst:
        new = re.findall(r"\d+", x)
        val[c] = new
        tempW = int(val[c][1]) + int(val[c][3])
        tempH = int(val[c][2]) + int(val[c][4])
        if tempW > maxW:
            maxW = tempW
        if tempH > maxH:
            maxH = tempH
        c+= 1

    board = []
    def init():
        for x in range(maxH):
            row = []
            for y in range(maxW):
                row.append(0)
            board.append(row)
    init()

    for n in range(len(val)):
        for x in range(int(val[n][1]), int(val[n][3])+int(val[n][1])):
            for y in range(int(val[n][2]), int(val[n][4])+int(val[n][2])):
                board[x][y] += 1

    for x in board:
        for y in x:
            if y >= 2:
                num += 1

    """ Day 3 Part 2 """

    real = []
    for n in range(len(val)):
        area = int(val[n][3]) * int(val[n][4])
        counter = 0
        for x in range(int(val[n][1]), int(val[n][3]) + int(val[n][1])):
            for y in range(int(val[n][2]), int(val[n][4]) + int(val[n][2])):
                if board[x][y] == 1:
                    counter+= 1
        if area == counter:
            real += [int(val[n][0])]

    return num, real

print(overlap("day3_input.txt"))




