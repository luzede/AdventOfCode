import requests
from os.path import dirname, abspath, join
from inspect import getsourcefile
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

cookies = {
    "session": config.get("SESSION"),
}

response = requests.get("https://adventofcode.com/2023/day/5/input", cookies=cookies)
current_folder = dirname(abspath(getsourcefile(lambda:0)))

with open(join(current_folder, "almanac.txt"), 'w') as f:
    f.write(response.text)

    
