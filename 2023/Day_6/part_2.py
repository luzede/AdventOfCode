from os.path import dirname, abspath, join
from inspect import getsourcefile
import re

current_folder = dirname(abspath(getsourcefile(lambda:0)))

document = open(join(current_folder, "document.txt"), "r")
time = int("".join(re.findall(r"\d+", document.readline())))
distance = int("".join(re.findall(r"\d+", document.readline())))

# Using binary search
i = 0
j = int(time/2)
while i < j:
    m = int((i+j)/2)
    if m*(time-m) > distance:
        j = m
    else:
        i = m + 1

k = int(time/2)
l = time
while k < l:
    m = int((k+l)/2)
    if m*(time - m) > distance:
        k = m + 1
    else:
        l = m
        
print(k - i)
        

