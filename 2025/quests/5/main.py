def print_fish(fish):
    for row in fish:
        print(row)
    # print()

with open('1.in', 'r') as f:
    data = f.read().strip()
    parts = data.split(':')
    nums = [int(x) for x in parts[1].split(',')]
    fish = [[-1, -1, -1]]
    for num in nums:
        for row in fish:
            if row[1] == -1:
                row[1] = num
                break
            elif row[0] ==- 1 and num < row[1]:
                row[0] = num
                break
            elif row[2] == -1 and num > row[1]:
                row[2] = num
                break
        else:
            fish.append([-1, num, -1])

    print(''.join([str(x[1]) for x in fish]))

def line_score(line):
    parts = line.split(':')
    nums = [int(x) for x in parts[1].split(',')]
    fish = [[-1, -1, -1]]
    for num in nums:
        for row in fish:
            if row[1] == -1:
                row[1] = num
                break
            elif row[0] ==- 1 and num < row[1]:
                row[0] = num
                break
            elif row[2] == -1 and num > row[1]:
                row[2] = num
                break
        else:
            fish.append([-1, num, -1])

    return int(''.join([str(x[1]) for x in fish]))

with open('2.in', 'r') as f:
    data = f.read().strip()
    lines = data.splitlines()
    fish_quals = [line_score(line) for line in lines]
    print(max(fish_quals) - min(fish_quals))

def fish_quality(fish):
    return int(''.join([str(x[1]) for x in fish]))

def make_fish(line):
    parts = line.split(':')
    id = int(parts[0])
    nums = [int(x) for x in parts[1].split(',')]
    fish = [[-1, -1, -1]]
    for num in nums:
        for row in fish:
            if row[1] == -1:
                row[1] = num
                break
            elif row[0] ==- 1 and num < row[1]:
                row[0] = num
                break
            elif row[2] == -1 and num > row[1]:
                row[2] = num
                break
        else:
            fish.append([-1, num, -1])
    return id, fish

from functools import cmp_to_key


def compare(a, b):
    id_a, fish_a = a
    id_b, fish_b = b
    qual_a = fish_quality(fish_a)
    qual_b = fish_quality(fish_b)
    if qual_a != qual_b:
        return qual_a - qual_b

    for i in range(len(fish_a)):
        row_a = int(''.join([str(x) if x != -1 else '' for x in fish_a[i]]))
        row_b = int(''.join([str(x) if x != -1 else '' for x in fish_b[i]]))
        if row_a != row_b:
            return row_a - row_b
    return id_a - id_b


with open('3.in', 'r') as f:
    data = f.read().strip()
    lines = data.splitlines()
    fishes = []
    for line in lines:
        id, fish = make_fish(line)
        fishes.append((id, fish))

    ans = 0
    fishes.sort(key=cmp_to_key(compare))
    for i in range(len(fishes)):
        id, fish = fishes[i]
        ans += id * (len(fishes)-i)
        # print(id, len(fishes) - i)
        # print_fish(fish)
        # print(fish_quality(fish))
        # print()
    print(ans)
