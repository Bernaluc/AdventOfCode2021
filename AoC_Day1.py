with open('input_day1.txt') as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(int(line.strip()))

print(data)

count = 0
for index in range(len(data) - 1):
    if data[index + 1] > data[index]:
        count += 1

print ("Counts: ", count)

sums = []
for index in range(len(data) - 2):
    sums.append(data[index] + data[index + 1] + data[index + 2])

sum_count = 0;
for index in range(len(sums)-1):
    if sums[index + 1] > sums[index]:
        sum_count += 1

print("Sum count: ", sum_count)
