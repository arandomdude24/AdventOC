'''
Ishaan Patel
Advent Of Code - 2018, Day 2
'''

def checksum(fileName):
    """ Day 2 Part 1 Function """
    lst = open(fileName, 'r').readlines()
    double = triple = 0

    for x in lst:
        dct = {}
        twoDone = False
        tripDone = False

        for i in x:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1

        for a in dct:
            if dct[a] == 2:
                twoDone = True
            if dct[a] == 3:
                tripDone = True

        double += int(twoDone)
        triple += int(tripDone)
    return double * triple


def diff(fileName):
    """ Day 2 Part 2 Function """
    lst = open(fileName, 'r').readlines()
    for x in lst:
        for y in lst:
            dif = 0
            char = ''
            for i in range(len(y)-1):
                if y[i] != x[i]:
                    dif+= 1
                else:
                    char+= y[i]
            if dif == 1:
                val = char
                return val

print(checksum('day2_input.txt'))
print(diff('day2_input.txt'))








