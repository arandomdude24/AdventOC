"""
Ishaan Patel
12/21/2018
Advent of Code - Day 5
"""

def reduce(fileName):
    """ Part 1: Returns how long the polymer is after
    going through all the reactions"""

    lst = open(fileName, 'r').readlines()
    large = []
    val = []

    for x in lst:
        for y in x:
            large.append(y)

    again = large

    def react(str):
        """ Reacts the given string and returns the length """
        first = ''
        second = ''
        done = False
        c = 0
        ind = []
        while not done:
            for i in range(len(str)):
                first = second
                second = str[i]
                if first.lower() == second.lower():
                    if first != second:
                        if i not in ind and  i-1 not in ind:
                            ind.append(i - 1)
                            ind.append(i)

            ind.sort(reverse = True)

            if ind:
                for x in ind:
                    del str[x]
                ind = []
            else:
                return len(str) + 18

    """ Part 2 """
    for x in range(65, 91):
        copy = again
        while chr(x) or chr(x+32) in again:
            if chr(x) in again:
                copy.remove(chr(x))
            if chr(x+32) in again:
                copy.remove(chr(x+32))
        val.append(react(copy))

    return min(val)

print(reduce("day5_input.txt"))
print(reduce("test.txt"))