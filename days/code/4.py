from loadinput import loadinput
from collections import defaultdict
DAY = 4


input = loadinput(DAY).split('\n')
total = 0
N = defaultdict(int)
for i, line in enumerate(input):
    N[i] += 1
    lists = line.split(':')[1].split('|')
    lists = [l.strip() for l in lists]
    winning_numbers = [int(n.strip()) for n in lists[0].split()]
    numbers = [int(n.strip()) for n in lists[1].split()]
    val = len(set(winning_numbers) & set(numbers))
    for j in range(val):
        N[i+1+j] += N[i]
    a = 0
    for number in winning_numbers:
        if number in numbers:
            a+=1
    total += 2**(a-1) if a != 0 else 0
print(total)
print(sum(N.values()))