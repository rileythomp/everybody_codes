with open('1.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    names = lines[0].split(',')
    instructions = lines[-1].split(',')
    cur_name = 0
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        cur_name = min(len(names)-1, (cur_name + distance)) if direction == 'R' else max(0, (cur_name - distance))
    print(names[cur_name])

with open('2.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    names = lines[0].split(',')
    instructions = lines[-1].split(',')
    cur_name = 0
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        cur_name = (cur_name + (distance if direction == 'R' else -distance)) % len(names)
    print(names[cur_name])

with open('3.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    names = lines[0].split(',')
    instructions = lines[-1].split(',')
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        next_name = distance % len(names) if direction == 'R' else (len(names) - distance) % len(names)
        names[0], names[next_name] = names[next_name], names[0]
    print(names[0])


