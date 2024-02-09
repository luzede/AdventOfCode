import requests
from os.path import dirname, abspath, join
from inspect import getsourcefile
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

session = config.get("SESSION")

cookies = {
    "session": session
}

response = requests.get(url="https://adventofcode.com/2023/day/4/input", cookies=cookies)

current_folder = dirname(abspath(getsourcefile(lambda:0)))

with open(join(current_folder, "cards.txt"), 'w') as f:
    f.write(response.text)
