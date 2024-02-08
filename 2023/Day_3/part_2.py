from os.path import dirname, abspath, join
from inspect import getsourcefile

current_folder = dirname(abspath(getsourcefile(lambda:0)))

schematic = None
with open(join(current_folder, "schematic.txt"), 'r') as f:
    schematic = list(map(
        lambda s: ['.', *list(s), '.'],
        f.read().splitlines()
    ))

n = len(schematic[0])
schematic = [
    ['.']*n,
    *schematic,
    ['.']*n
]
m = len(schematic)

# 3D
schem_map = [[[] for _ in range(n)] for _ in range(m)]

digits = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" }

def populate_border(i, fi, li, number):
    for k in range(i-1, i+2):
        for l in range(fi-1, li+2):
            schem_map[k][l].append(number)
            
    

for i in range(1, m):
    digit_array = []
    # First digit index
    fdi = None
    for j in range(1, n):
        char = schematic[i][j]
        if char not in digits:
            continue
        digit_array.append(char)
        if fdi is None:
            fdi = j
        if schematic[i][j+1] not in digits and fdi is not None:
            number = int("".join(digit_array))
            print(number)
            populate_border(i, fdi, j, number)
            digit_array = []
            fdi = None
         

gear_ratio_sum = 0    
for i in range(1, m):
    for j in range(1, n):
        char = schematic[i][j]
        if char == "*" and len(schem_map[i][j]) == 2:
            num1 = int(schem_map[i][j][0])
            num2 = int(schem_map[i][j][1])
            gear_ratio = num1*num2
            gear_ratio_sum += gear_ratio
            
print(gear_ratio_sum)
            
            
            
