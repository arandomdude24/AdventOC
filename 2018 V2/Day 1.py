"""
Ishaan Patel
Advent Of Code 2018 - Day 1 V2
5/20/19
"""

FILE = 'day1_input.txt'
lst = open(FILE, 'r').readlines()

'''Part 1, returns the sum of all values'''
val = 0
for x in lst:
    val += int(x)
print(val)

'''Part 2, returns the first sum to be seen twice'''
val = 0
sums = {}
result = 0
done = False
while not done:
    for x in lst:
        if val in sums:
            done = True
            result = val
        else:
            sums[val] = 1
            val += int(x)
print(result)