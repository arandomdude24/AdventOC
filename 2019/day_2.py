def intcode(file, one, two):
    input = open(file, 'r').readline()
    lst = [int(n) for n in input.split(',')]
    index = 0
    lst[1] = one
    lst[2] = two
    while lst[index] != 99:
        if lst[index] == 1:
            val = lst[lst[index+1]] + lst[lst[index+2]]
        else:
            val = lst[lst[index+1]] * lst[lst[index+2]]
        lst[lst[index + 3]] = val
        index += 4
    return lst[0]

def complex_intcode(file):
    for x in range(100):
        for y in range(100):
            if intcode(file, x, y) == 19690720:
                return 100*x+y

print(intcode('day2_input.txt', 12, 2))
print(complex_intcode('day2_input.txt'))

