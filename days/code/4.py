from loadinput import loadinput

DAY = 4


input = loadinput(DAY).split('\n')
total = 0
or i, line in enumerate(input):
    lists = line.split(':')[1].split('|')
    lists = [l.strip() for l in lists]
    winning_numbers = [int(n.strip()) for n in lists[0].split()]
    numbers = [int(n.strip()) for n in lists[1].split()]
    a = 0
    for number in winning_numbers:
        if number in numbers:
            a+=1
    total += 2**(a-1) if a != 0 else 0
print(total)