from os.path import dirname, abspath, join
from inspect import getsourcefile
import requests
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

session = config.get("SESSION")

current_folder = dirname(abspath(getsourcefile(lambda:0)))

with open(join(current_folder, "hands_and_bids.txt"), "w") as f:
    response = requests.get("https://adventofcode.com/2023/day/7/input", cookies={ "session": session })
    f.write(response.text)
