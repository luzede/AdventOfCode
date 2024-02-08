import requests
from os.path import abspath, dirname, join
from inspect import getsourcefile
from dotenv import find_dotenv, dotenv_values

current_folder = dirname(abspath(getsourcefile(lambda:0)))

config = dotenv_values(find_dotenv())
session = config.get("SESSION")
cookies = {
    "session": session
}

response = requests.get(
    url="https://adventofcode.com/2023/day/3/input",
    cookies=cookies
)

with open(join(current_folder, 'schematic.txt'), 'w') as f:
    f.write(response.text)
