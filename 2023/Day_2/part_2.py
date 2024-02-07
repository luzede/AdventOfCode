from os.path import dirname, abspath, join
from inspect import getsourcefile
import re

current_folder = dirname(abspath(getsourcefile(lambda:0)))

game_records = open(join(current_folder, "game_records.txt"), "r")

reg_string = r"(?P<amount>\d+) (?P<color>red|green|blue)"
pattern = re.compile(pattern=reg_string)


cube_set_power_sum = 0

for line in game_records:
    matches = re.finditer(pattern, line)
    # Maximum number of cubes in a round
    max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for match in matches:
        color = match["color"]
        amount = int(match["amount"])
        max_cubes[color] = max(max_cubes[color], amount)
    
    cube_set_power = max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]
    cube_set_power_sum += cube_set_power


game_records.close()

print(cube_set_power_sum)