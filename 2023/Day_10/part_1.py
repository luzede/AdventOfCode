from os.path import dirname, join
from inspect import getsourcefile
from math import ceil
from collections import deque
from collections import defaultdict

current_folder = dirname(getsourcefile(lambda:0))

tiles_grid = None
with open(join(current_folder, "tiles_grid.txt"), "r") as f:
    tiles_grid = [list(line) for line in f.read().splitlines()]


start = None
for i in range(len(tiles_grid)):
    if start is not None: break
    for j in range(len(tiles_grid[0])):
        if tiles_grid[i][j] == "S":
            start = (i, j)
            break

m = len(tiles_grid)
n = len(tiles_grid[0])

connected = {
    ("|", "N", "|"), ("|", "S", "|"), ("|", "S", "L"), ("|", "S", "J"), ("|", "N", "7"), ("|", "N", "F"),
    ("-", "E", "-"), ("-", "W", "-"), ("-", "E", "J"), ("-", "W", "L"), ("-", "E", "7"), ("-", "W", "F"),
    ("L", "N", "|"), ("L", "E", "-"), ("L", "E", "J"), ("L", "E", "7"), ("L", "N", "7"), ("L", "N", "F"),
    ("J", "N", "|"), ("J", "W", "-"), ("J", "W", "L"), ("J", "N", "7"), ("J", "N", "F"), ("J", "W", "F"),
    ("7", "S", "|"), ("7", "W", "-"), ("7", "W", "L"), ("7", "S", "L"), ("7", "S", "J"), ("7", "W", "F"),
    ("F", "S", "|"), ("F", "E", "-"), ("F", "S", "L"), ("F", "S", "J"), ("F", "E", "J"), ("F", "E", "7")
}
connections = defaultdict(set)

for i in range(m):
    for j in range(n):
        char = tiles_grid[i][j]
        if char == ".": continue
        east = j+1 if j+1 < n else n-1
        west = j-1 if j-1 >= 0 else 0
        north = i-1 if i-1 >= 0 else 0
        south = i+1 if i+1 < m else m-1
        char_e = tiles_grid[i][east]
        char_w = tiles_grid[i][west]
        char_n = tiles_grid[north][j]
        char_s = tiles_grid[south][j]
        if (char, "E", char_e) in connected:
            connections[(i,j)].add((i,east))
            connections[(i,east)].add((i,j))
        if (char, "W", char_w) in connected:
            connections[(i,j)].add((i,west))
            connections[(i,west)].add((i,j))
        if (char, "N", char_n) in connected:
            connections[(i,j)].add((north,j))
            connections[(north,j)].add((i,j))
        if (char, "S", char_s) in connected:
            connections[(i,j)].add((south,j))
            connections[(south,j)].add((i,j))
        
max_distance = 0

for char in ["|", "-", "L", "J", "7", "F"]:
    i, j = start
    east = j+1 if j+1 < n else n-1
    west = j-1 if j-1 >= 0 else 0
    north = i-1 if i-1 >= 0 else 0
    south = i+1 if i+1 < m else m-1
    char_e = tiles_grid[i][east]
    char_w = tiles_grid[i][west]
    char_n = tiles_grid[north][j]
    char_s = tiles_grid[south][j]

    if (char, "E", char_e) in connected:
        connections[(i,j)].add((i,east))
        connections[(i,east)].add((i,j))
    if (char, "W", char_w) in connected:
        connections[(i,j)].add((i,west))
        connections[(i,west)].add((i,j))
    if (char, "N", char_n) in connected:
        connections[(i,j)].add((north,j))
        connections[(north,j)].add((i,j))
    if (char, "S", char_s) in connected:
        connections[(i,j)].add((south,j))
        connections[(south,j)].add((i,j))
        
    if len(connections[start]) != 2:
        if (char, "E", char_e) in connected:
            connections[(i,j)].remove((i,east))
            connections[(i,east)].remove((i,j))
        if (char, "W", char_w) in connected:
            connections[(i,j)].remove((i,west))
            connections[(i,west)].remove((i,j))
        if (char, "N", char_n) in connected:
            connections[(i,j)].remove((north,j))
            connections[(north,j)].remove((i,j))
        if (char, "S", char_s) in connected:
            connections[(i,j)].remove((south,j))
            connections[(south,j)].remove((i,j))
        continue

    visited = defaultdict(lambda:False)
    distance = 0
    q = deque([(start, 0)])
    while len(q):
        pos, dist = q.pop()
        if visited[pos] and pos == start and distance > 2:
            distance = dist
            break
        if visited[pos]: continue
        visited[pos] = True
        distance = max(dist, distance)
        for next_pos in connections[pos]:
            q.append((next_pos, dist+1))
    
    max_distance = max(max_distance, distance)
    
    

print(ceil(distance/2))