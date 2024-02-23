from os.path import dirname, join
from inspect import getsourcefile

current_folder = dirname(getsourcefile(lambda:0))

oasis_report = open(join(current_folder, "oasis_report.txt"), "r")


extrapolated_value_sum = 0

for line in oasis_report:
    values = list(map(lambda v: int(v), line.split()))[::-1]
    pyramid = []
    while any(values):
        next_values = []
        for i in range(1, len(values)):
            next_values.append(values[i] - values[i-1])
        pyramid.append(values)
        values = next_values
    
    for i in range(len(pyramid) - 1, 0, -1):
        pyramid[i-1].append(pyramid[i-1][-1] + pyramid[i][-1])
    extrapolated_value_sum += pyramid[0][-1]
        
oasis_report.close()

print(extrapolated_value_sum)