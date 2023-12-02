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
    _, info = line.split(': ')
    possible = True
    for subset in info.split('; '):
        # reset the count every iteration
        red_count = MAX_RED
        green_count = MAX_GREEN
        blue_count = MAX_BLUE
        # parse the cubes
        cubes = subset.split(', ')
        cubes = [cube.split(' ') for cube in cubes]
        # iterate through the cubes and check if they are possible
        for (count, color) in cubes:
            count = int(count)
            if color == 'red':
                red_count -= count
            elif color == 'green':
                green_count -= count
            else:
                blue_count -= count

            if any(num < 0 for num in [red_count, green_count, blue_count]):
                possible = False
                break
    # increase by the index if the game's possible
    res += i if possible else 0
print(res)
