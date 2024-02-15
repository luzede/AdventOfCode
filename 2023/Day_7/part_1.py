from os.path import dirname, abspath, join
from inspect import getsourcefile
import re
from collections import Counter

current_folder = dirname(abspath(getsourcefile(lambda:0)))

card_strength = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

hands_and_bids = open(join(current_folder, "hands_and_bids.txt"), 'r')

hands = []
bids = []

for line in hands_and_bids:
    m = re.match(r"(?P<hand>[\w\d]+) (?P<bid>\d+)", line)
    hands.append(m['hand'])
    bids.append(int(m['bid']))

hands_and_bids.close()

transformed_hands = []
for hand, bid in zip(hands, bids):
   freq = Counter(hand)
   transformed_hand = tuple(sorted(freq.values(), reverse=True)) + tuple(map(lambda c: card_strength[c], hand))
   transformed_hands.append((transformed_hand, bid))

transformed_hands.sort()

total_winnings = 0
for i in range(0, len(transformed_hands)):
    total_winnings += (i+1)*transformed_hands[i][1]

print(total_winnings)
   
   


