from loadinput import loadinput

DAY = 6

times, distances = [list(map(int, ["".join(line.split(":")[1].split())])) for line in loadinput(DAY).split('\n')]

result = 1

for time, distance in zip(times, distances):
    margin = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            margin += 1
    result *= margin

print(result)