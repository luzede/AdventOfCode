from os.path import abspath, dirname, join
from inspect import getsourcefile
import re

current_folder = dirname(abspath(getsourcefile(lambda:0)))

game_records = open(join(current_folder, "game_records.txt"), 'r')

reg_string = r"(?P<amount>\d+) (?P<color>red|blue|green)"
pattern = re.compile(pattern=reg_string)

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game_id = 1
game_id_sum = 0
for line in game_records:
    matches = re.finditer(pattern, line)
    game_id_sum += game_id
    for match in matches:
        color = match["color"]
        amount = int(match["amount"])
        if max_cubes[color] < amount:
            game_id_sum -= game_id
            break
    game_id += 1

game_records.close()

print(game_id_sum)