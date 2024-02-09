from os.path import dirname, abspath, join
from inspect import getsourcefile
import re

current_folder = dirname(abspath(getsourcefile(lambda:0)))

cards = open(join(current_folder, "cards.txt"), 'r')

reg_string = r":\s+(?P<numbers>[\d\s]+)\|\s+(?P<winning>.+)"
pattern = re.compile(pattern=reg_string)


total_points = 0
for line in cards:
    m = re.search(pattern, line)
    numbers = list(map(lambda s: int(s), m['numbers'].split()))
    winning = set(map(lambda s: int(s), m["winning"].split()))
    # print(winning)
    # print(numbers)
    count = 0
    for number in numbers:
        if number in winning:
            count += 1
    if count != 0:
        total_points += 2**(count - 1)
        
cards.close()

print(total_points)