from os.path import dirname, abspath, join
from inspect import getsourcefile
import re

current_folder = dirname(abspath(getsourcefile(lambda:0)))

cards = open(join(current_folder, "cards.txt"), 'r')

reg_string = r":\s+(?P<numbers>[\d\s]+)\|\s+(?P<winning>.+)"
pattern = re.compile(pattern=reg_string)


card_wincount = []
for line in cards:
    m = re.search(pattern, line)
    numbers = m["numbers"].split()
    winning = set(m["winning"].split())
    count = 0
    for number in numbers:
        if number in winning:
            count += 1
    card_wincount.append(count)

cards.close()

size = len(card_wincount)
card_count = [1]*size

for i, v in enumerate(card_count):
    for j in range(1,card_wincount[i]+1):
        card_count[i+j] += 1*card_count[i]
    

total_cards = sum(card_count)
print(total_cards)