from inspect import getsourcefile
from os.path import abspath, dirname, join

current_folder = dirname(abspath(getsourcefile(lambda:0)))

calibration_doc = open(join(current_folder, "calibration_doc.txt"), "r")

calibration_values_sum = 0
numbers_set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

for line in calibration_doc:
    first_digit = None
    last_digit = None
    for char in line:
        if char in numbers_set:
            first_digit = char
            break
    for i in range(len(line)-1, -1, -1):
        if line[i] in numbers_set:
            last_digit = line[i]
            break
    if first_digit is not None and last_digit is not None:
        calibration_values_sum += int(first_digit + last_digit)
    else:
        print(line)

calibration_doc.close()

print(calibration_values_sum)