from os.path import dirname, abspath, join
from inspect import getsourcefile
import re


current_folder = dirname(abspath(getsourcefile(lambda:0)))

almanac = open(join(current_folder, "almanac.txt"), 'r')

seeds = list(map(lambda s: int(s), re.findall(r"\d+", almanac.readline())))

reg_string = r"{}|{}".format(
    r"(?P<s_name>\w+)-to-(?P<d_name>\w+) map:",
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
        srs = int(m['srs'])
        drs = int(m['drs'])
        rl = int(m['rl'])
        s_to_d_map[(s_name, d_name)].append((srs, drs, rl))

almanac.close()


def transform(s, s_name, d_name):
    for (srs, drs, rl) in s_to_d_map[(s_name, d_name)]:
        if (s >= srs) and (s < srs + rl):
            offset = s - srs
            return drs + offset
    return s
            
    

start = "seed"
start_list = list(seeds)
while start != "location":
    dest = sn_to_dn_map[start]
    start_list = [transform(x, start, dest) for x in start_list]
    start = dest
    
print(min(start_list))
    
    
