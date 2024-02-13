from os.path import dirname, join, abspath
from inspect import getsourcefile
import requests
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

session = config.get("SESSION")

cookies = {
    "session": session
}

current_folder = dirname(abspath(getsourcefile(lambda:0)))

with open(join(current_folder, "document.txt"), "w") as f:
    response = requests.get("https://adventofcode.com/2023/day/6/input", cookies=cookies)
    f.write(response.text)