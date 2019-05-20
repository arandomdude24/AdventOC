'''
Ishaan Patel
Advent Of Code - 2018, Day 1
'''

def sum(fileName):
    """ Part 1 """
    val = 0
    lst = open(fileName, 'r').readlines()
    for x in lst:
        val += int(x)
    return val

def duplicate(fileName):
    """ Part 2"""
    val = 0
    freq = []
    lst = open(fileName, 'r').readlines()
    c = 0

    while True:
        for x in lst:
            val += int(x)
            if not c:
                freq.append(val)
            elif val in freq:
                return val
        c += 1

print(sum('day1_input.txt'))
print(duplicate('day1_input.txt'))



