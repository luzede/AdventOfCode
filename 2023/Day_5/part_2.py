from os.path import dirname, abspath, join
from inspect import getsourcefile
import re

current_folder = dirname(abspath(getsourcefile(lambda:0)))

almanac = open(join(current_folder, 'almanac.txt'), 'r')

seeds = list(map(
    lambda s: tuple(map(lambda i: int(i), s.split())),
    re.findall(r"\d+ \d+", almanac.readline())
))

reg_string = r"{}|{}".format(
    r"(?P<s_name>\w+)-to-(?P<d_name>\w+)",
    r"(?P<drs>\d+) (?P<srs>\d+) (?P<rl>\d+)"
)

pattern = re.compile(reg_string)

s_to_d_map = {}
sn_to_dn_map = {}

d_name = None
s_name = None
for line in almanac:
    m = re.match(pattern, line)
    if m is None:
        continue
    if m['d_name'] is not None:
        d_name = m['d_name']
        s_name = m['s_name']
        sn_to_dn_map[s_name] = d_name
        s_to_d_map[(s_name, d_name)] = []
    else:
        drs = int(m['drs'])
        srs = int(m['srs'])
        rl = int(m['rl'])
        s_to_d_map[(s_name, d_name)].append((srs, drs, rl))

almanac.close()

start = "seed"
start_list = list(seeds)
while start != "location":
    dest = sn_to_dn_map[start]
    dest_list = list()
    for (s, r) in start_list:
        size = len(start_list)
        fully_mapped = False
        for (srs, drs, rl) in s_to_d_map[(start, dest)]:
            if s >= srs and s + r <= srs + rl:
                offset = s - srs
                dest_list.append((drs + offset, r))
                fully_mapped = True
                break
            elif s < srs and srs+rl < s + r:
                offset_l = srs - s
                offset_r = s + r - srs - rl
                start_list.append((s, offset_l))
                start_list.append((srs + rl, offset_r))
                dest_list.append((drs, rl))
                break
            elif s + r > srs and s + r < srs + rl:
                offset = srs - s
                dest_list.append((drs, r - offset))
                start_list.append((s, offset))
                break
            elif s > srs and s < srs + rl:
                offset = s - srs
                dest_list.append((drs + offset, rl - offset))
                diff1 = srs + rl - s
                diff2 = s + r - srs - rl
                start_list.append((s+diff1, diff2))
                break
        if size == len(start_list) and not fully_mapped:
            dest_list.append((s, r))
    start_list = dest_list
    start = dest

print(sorted(start_list, key=lambda s: s[0])[0][0])