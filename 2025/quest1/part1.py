with open('part1.txt', 'r') as file:
    lines = file.read().strip().split('\n')
    names = lines[0].split(',')
    instructions = lines[-1].split(',')
    cur_name = 0
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        cur_name = min(len(names)-1, (cur_name + distance)) if direction == 'R' else max(0, (cur_name - distance))
    print(names[cur_name])

