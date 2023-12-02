import re
from loadinput import loadinput


DAY = 1
# Load the input
input = loadinput(DAY).split('\n')


count = 0
for line in input:
    map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    def convert_to_digits(match):
        word = match.group()
        return map.get(word, word)
    nums = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    nums = [map.get(num, num) for num in nums]
    count += int(nums[0] + nums[-1])
print(count)