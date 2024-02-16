from os.path import dirname, abspath, join
from inspect import getsourcefile
import re

current_folder = dirname(abspath(getsourcefile(lambda:0)))

maps = open(join(current_folder, "maps.txt"), 'r')

directions = maps.readline().strip()

map = {}

for line in maps:
    m = re.findall(r"\w+", line)
    if len(m) == 0: continue
    pos = m[0]
    left = m[1]
    right = m[2]
    map[pos] = (left, right)

maps.close()


start = 'AAA'
destination = 'ZZZ'

steps = 0
di = 0 # Direction Index

while start != destination:
    if (di == len(directions)): di = 0
    start = map[start][0 if directions[di] == 'L' else 1]
    steps += 1
    di += 1

print("Part 1:", steps)

