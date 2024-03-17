from os.path import dirname, join
from inspect import getsourcefile
import requests
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

session = config.get("SESSION")

current_folder = dirname(getsourcefile(lambda:0))

with open(join(current_folder, "tiles_grid.txt"), "w") as f:
    response = requests.get("https://adventofcode.com/2023/day/10/input", cookies={ "session": session })
    f.write(response.text)

