# This fetches the calibration document from the AdventOfCode and writes
# it into a file called "calibration_doc.txt" in the same folder



import requests
from dotenv import dotenv_values, find_dotenv
from inspect import getsourcefile
from os.path import abspath, dirname, join

current_folder = dirname(abspath(getsourcefile(lambda:0)))

# Loads .env variables, looks for .env file in current or parent folders
config = dotenv_values(find_dotenv())
session = config.get("SESSION")

cookies = {
    "session": session
}
response = requests.get(
    url="https://adventofcode.com/2023/day/1/input",
    cookies=cookies
)

with open(join(current_folder, "calibration_doc.txt"), 'w') as f:
    f.write(response.text)
