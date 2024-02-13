from os.path import dirname, join, abspath
from inspect import getsourcefile
import re

current_folder = dirname(abspath(getsourcefile(lambda:0)))

document = open(join(current_folder, "document.txt"), "r")

times = map(lambda s: int(s), re.findall(r"\d+", document.readline()))
distances = map(lambda s: int(s), re.findall(r"\d+", document.readline()))

document.close()

margin_of_error = 1
for time, distance in zip(times, distances):
    ways_to_beat = 0
    for i in range(1, time):
        if i*(time-i) > distance:
            ways_to_beat += 1
    margin_of_error *= ways_to_beat

print(margin_of_error)
    
