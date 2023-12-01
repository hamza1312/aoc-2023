from loadinput import loadinput


DAY = 1
# Load the input
input = loadinput(DAY).split('\n')

count = 0
for line in input:
    words = line.split()
    for word in words:
        first: str | None = None
        latest: str | None = None
        for index, ch in enumerate(word):
            if ch.isdigit():
               if not first:
                   first = ch
               latest = ch
        count += int(f'{first}{latest}')
# Then finally print the output
print(count)