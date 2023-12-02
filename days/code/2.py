import re
from loadinput import loadinput


DAY = 2
# Load the input
input = loadinput(DAY).split('\n')
# defining the constants
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

res = 0

for i, line in enumerate(input, 1):
    red = 0
    blue = 0
    green = 0
    _, info = line.split(': ')
    possible = True
    for subset in info.split('; '):
        # reset the count every iteration
        cubes = subset.split(', ')
        cubes = [cube.split(' ') for cube in cubes]
        # iterate through the cubes and check if they are possible
        for (count, color) in cubes:
            count = int(count)
            if color == 'red':
                red = max(red, count)
            elif color == 'green':
                green = max(green, count)
            else:
                blue = max(blue, count)
    res += red * blue * green
print(res)
