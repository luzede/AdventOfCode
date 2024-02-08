from os.path import dirname, abspath, join
from inspect import getsourcefile

current_folder = dirname(abspath(getsourcefile(lambda:0)))

schematic = None
with open(join(current_folder, "schematic.txt"), "r") as f:
    schematic = list(map(lambda s: ['.',*list(s),'.'], f.read().splitlines()))

schematic= [
    ['.']*len(schematic[0]),
    *schematic,
    ['.']*len(schematic[0])
]

m = len(schematic)
n = len(schematic[0])

digits = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" }

# fi: First Index, li: Last Index, i: Line Index 
def is_part_number(i, fi, li):
    if schematic[i][fi - 1] != '.':
        return True
    if schematic[i][li + 1] != '.':
        return True
    for j in range(fi-1, li+2):
        if schematic[i-1][j] != '.':
            return True
    for j in range(fi-1, li+2):
        if schematic[i+1][j] != '.':
            return True
    return False

part_numbers = []

for i in range(1,m):
    digit_array = []
    # First digit index
    fdi = None
    for j in range(1,n):
        char = schematic[i][j]
        if char not in digits:
            continue
        digit_array.append(char)
        if fdi is None:
            fdi = j
        if schematic[i][j+1] not in digits and fdi != None:
            if is_part_number(i, fdi, j):
                part_number = int("".join(digit_array))
                part_numbers.append(part_number)
            digit_array = []
            fdi = None

print(sum(part_numbers))