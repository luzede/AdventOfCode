import re
from inspect import getsourcefile
from os.path import abspath, dirname, join


current_folder = dirname(abspath(getsourcefile(lambda:0)))

calibration_doc = open(join(current_folder, "calibration_doc.txt"), 'r')

reg_string = r"{}({}{}{}|{}){}".format(
    r"^.*?",
    r"(one|two|three|four|five|six|seven|eight|nine|\d)",
    r".*",
    r"(one|two|three|four|five|six|seven|eight|nine|\d)",
    r"(one|two|three|four|five|six|seven|eight|nine|\d)",
    r".*\n$"
)
pattern = re.compile(reg_string)

word_to_digit_map = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

calibration_values_sum = 0

for line in calibration_doc:
    m = re.match(pattern, line)
    # Since I know that the regex will definitely match
    # There is no reason to check if "m" is True
    if m.group(2):
        first_digit = word_to_digit_map[m.group(2)]
        last_digit = word_to_digit_map[m.group(3)]
        calibration_values_sum += int(first_digit + last_digit)
    else:
        digit = word_to_digit_map[m.group(4)]
        calibration_values_sum += int(digit+digit)


calibration_doc.close()

print(calibration_values_sum)