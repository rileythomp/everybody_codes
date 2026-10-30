
with open('1.in', 'r') as f:
    data = f.read().strip()
    nums = [int(x) for x in data.split('\n')]
    print(2025*nums[0]//nums[-1])

from math import ceil

with open('2.in', 'r') as f:
    data = f.read().strip()
    nums = [int(x) for x in data.split('\n')]
    print(ceil(10000000000000*nums[-1]/nums[0]))

