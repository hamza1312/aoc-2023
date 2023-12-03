
from loadinput import loadinput

DAY = 3


grid = loadinput(DAY).split('\n')
cs = set()

for y, line in enumerate(grid):
    for x, ch in enumerate(line):
        if ch == '.' or ch.isdigit():
            continue
        for yd in [y - 1, y, y + 1]:
            for xd in [x - 1, x, x  + 1]:
                if yd < 0 or yd >= len(grid) or xd < 0 or xd >= len(grid[yd]) or not grid[yd][xd].isdigit():
                    continue    
                while xd > 0 and grid[yd][xd - 1].isdigit():
                    xd -= 1
                cs.add((yd, xd))

ns = []
for r, c in cs:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))

print(sum(ns))