with open('part3.txt', 'r') as file:
    lines = file.read().strip().split('\n')
    names = lines[0].split(',')
    instructions = lines[-1].split(',')
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        next_name = distance % len(names) if direction == 'R' else (len(names) - distance) % len(names)
        names[0], names[next_name] = names[next_name], names[0]
    print(names[0])

