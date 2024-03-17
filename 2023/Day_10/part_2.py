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

visited = [[0 for _ in range(n)] for _ in range(m)]

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

    tiles_grid[i][j] = char
    visited_set = set()
    q = deque([start])
    while len(q):
        pos = q.pop()
        k, l = pos
        visited[k][l] = 1
        if pos in visited_set: continue
        visited_set.add(pos)
        for next_pos in connections[pos]:
            q.append(next_pos)
    
    
for line in visited:
    print(line)        

tiles_enclosed_by_loop = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 1: tiles_enclosed_by_loop += 1
print(ceil(tiles_enclosed_by_loop/2))

#   Find a position where 0 is outside
# the area enclosed by the loop
#   We do this by looking for a 0 on
# the borders of the tiles_grid

grid_border_filled = False
while not grid_border_filled:
    zero_pos = None
    for i in range(m):
        for j in range(n):
            if zero_pos is not None: break
            if j == 0 or j == n-1:
                if visited[i][j] == 0: zero_pos = (i, j)
                break            
            if i != 0 or i != m-1: break
            if visited[i][j] == 0: zero_pos = (i, j)
    if zero_pos == None:
        grid_border_filled = True
        break
    else:
        print(zero_pos)

    q = deque([zero_pos])
    while len(q):
        pos = q.pop()
        if visited[pos[0]][pos[1]] == 1: continue
        visited[pos[0]][pos[1]] = 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if pos[0]+i < 0 or pos[0]+i >= m: continue
                if pos[1]+j < 0 or pos[1]+j >= n: continue
                q.append((pos[0]+i, pos[1]+j))


tiles_enclosed_by_loop = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0: tiles_enclosed_by_loop += 1

print(tiles_enclosed_by_loop)
     