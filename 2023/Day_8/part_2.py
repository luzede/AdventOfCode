from os.path import dirname, abspath, join
from inspect import getsourcefile
import re
from functools import reduce
import math

current_folder = dirname(abspath(getsourcefile(lambda:0)))

maps = open(join(current_folder, "maps.txt"), 'r')

directions = maps.readline().strip()

mapping = {}

for line in maps:
    m = re.findall(r"\w+", line)
    if len(m) == 0: continue
    pos = m[0]
    left = m[1]
    right = m[2]
    mapping[pos] = (left, right)

maps.close()

starts = list(filter(lambda p: p.endswith('A'),  mapping.keys()))
steps = [0]*len(starts)

for i in range(len(starts)):
    start = starts[i]
    di = 0
    step = 0
    while not start.endswith('Z'):
        if di == len(directions): di = 0
        start = mapping[start][0 if directions[di] == 'L' else 1]
        di += 1
        step += 1
    steps[i] = step

def lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers)

print(lcm(steps))
