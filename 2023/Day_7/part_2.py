from os.path import dirname, abspath, join
from inspect import getsourcefile
import re
from collections import Counter


current_folder = dirname(abspath(getsourcefile(lambda:0)))

card_strength = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}

hands = []
bids = []

hands_and_bids = open(join(current_folder, "hands_and_bids.txt"), 'r')

for line in hands_and_bids:
    m = re.match(r"(?P<hand>[\w\d]+) (?P<bid>\d+)", line)
    hands.append(m['hand'])
    bids.append(int(m['bid']))

hands_and_bids.close()

transformed_hands = []
for hand, bid in zip(hands,bids):
    freq = Counter(hand)
    j_count = 0
    if 'J' in hand and freq['J'] != 5:
        j_count = freq['J']
        del freq['J']
    sorted_freq_values = sorted(freq.values(), reverse=True)
    sorted_freq_values[0] += j_count
    transformed_hand = tuple(sorted_freq_values) + tuple(map(lambda c: card_strength[c], hand)) 
    transformed_hands.append((transformed_hand, bid))

transformed_hands.sort()

total_winnings = 0
for i in range(0, len(transformed_hands)):
    total_winnings += (i+1)*transformed_hands[i][1]
print(total_winnings)

