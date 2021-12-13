import re


with open('input_day2.txt') as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(line.strip())
#print(data)

class Submarine:
    "This class represents the submarine for Advent of Code used for Day 2"


    def __init__(self, x_init, y_init, z_init):
        self._xpos = 0
        self._ypos = 0
        self._zpos = 0
        self._aim = 0

    def mov_x(self, distance):
        self._xpos += distance
        self._zpos += self._aim * distance

    def mov_y(self, distance):
        self._ypos += distance

    # def mov_z(self, distance):
    #     self._aim += distance
    #     self._zpos += distance

    def mov_aim(self, distance):
        self._aim += distance

    def get_pos(self):
        return(self._xpos, self._ypos, self._zpos)

sub = Submarine(0, 0, 0)

for command in data:
    number = int(re.findall("[0-9]", command)[0]) #returns a list so using [0] to get string

    if "forward" in command:
        sub.mov_x(number)

    elif "down" in command:
        sub.mov_aim(number)

    elif "up" in command:
        sub.mov_aim(-number)

horizontal_pos, y, depth = sub.get_pos()

print(horizontal_pos*depth)