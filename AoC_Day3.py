import re

with open('input_day3.txt') as f:
    lines = f.readlines()

data = []
bools = []
for line in lines:
    data.append(line.strip())

for line in data:
    for num in line:
        bools.append(num)

counts = [0]*len(data[0])
for line in data:
    pos = 0
    for num in line:
        if num == "1":
            counts[pos] += 1
        pos +=1

print(counts)

zeros = []
ones = []

for i in counts:
    if i > int(len(data)/2):
        zeros.append(1)
        ones.append(0)
    else:
        zeros.append(0)
        ones.append(1)

print(zeros)
print(ones)



