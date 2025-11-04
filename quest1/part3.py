with open('part3.txt', 'r') as file:
    lines = file.read().strip().split('\n')
    names = lines[0].split(',')
    instructions = lines[-1].split(',')
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        top_name = 0
        next_name = 0
        if direction == 'R':
            next_name = distance % len(names)
        elif direction == 'L':
            next_name = (len(names) - distance) % len(names)
        names[top_name], names[next_name] = names[next_name], names[top_name]
    print(names[0])

