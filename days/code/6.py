from loadinput import loadinput

DAY = 6

time, distance = loadinput(DAY).split('\n')
time = [int(t) for t in time.split(':')[1].split()]
distance = [int(d) for d in distance.split(':')[1].split()]
result = 1


def calc(t, d):
    res = 0
    for x in range(t + 1):
        distancex = x * (t - x)
        if distancex >= d:
            res += 1
    return res


for i in range(len(time)):
    result *= calc(time[i], distance[i])

print(result)
