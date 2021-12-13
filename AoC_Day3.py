import re

with open('input_day2.txt') as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(line.strip())

    num_1 = re.findall('1', line)
    num_2 = re.findall('0', line)

    print(num_1)
    print(num_2)