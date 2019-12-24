
def formula_sum(file):
    """Part 1"""
    lst = open(file, 'r').readlines()
    sum = 0
    for number in lst:
        sum += (int(number)// 3) - 2
    return sum

def modified_sum(file):
    """ Part 2 """
    lst = open(file, 'r').readlines()
    sum = 0
    for number in lst:
        val = int(number)//3 - 2
        while val > 0:
            sum += val
            val = val//3 - 2
    return sum

print(formula_sum('day1_input.txt'))
print(modified_sum('day1_input.txt'))