from loadinput import loadinput

DAY = 5

seeds, *blocks = loadinput(DAY).split('\n\n')
seeds = [int(seed) for seed in seeds.split(': ')[1].split()]

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append([int(n) for n in line.split()])
    new = []
    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b + c:
                new.append(x - b + a)
                break
        else:
            new.append(x)
    seeds = new
print(min(seeds))