def multiply(x1, y1, x2, y2):
    return x1 * x2 - y1 * y2, x1 * y2 + y1 * x2

def divide(x1, y1, x2, y2):
    return int(x1 / x2), int(y1 / y2)

def add(x1, y1, x2, y2):
    return x1 + x2, y1 + y2

with open('1.in', 'r') as file:
    line = file.readline().strip()
    parts = line.split(',')
    ax = int(parts[0].split('[')[-1])
    ay = int(parts[1].split(']')[0])
    rx, ry = 0, 0
    for i in range(3):
        rx, ry = multiply(rx, ry, rx, ry)
        rx, ry = divide(rx, ry, 10, 10)
        rx, ry = add(rx, ry, ax, ay)
    print(rx, ry)

with open('2.in', 'r') as file:
    line = file.readline().strip()
    parts = line.split(',')
    x0 = int(parts[0].split('[')[-1])
    y0 = int(parts[1].split(']')[0])
    x1, y1 = add(x0, y0, 1000, 1000)
    coords = []
    for y in range(y0, y1+1, 10):
        for x in range(x0, x1+1, 10):
            coords.append((x, y))
    ans = 0
    engrave = {}
    for x, y in coords:
        should_engrave = True
        rx, ry = 0, 0
        for i in range(100):
            rx, ry = multiply(rx, ry, rx, ry)
            rx, ry = divide(rx, ry, 100000,100000)
            rx, ry = add(rx, ry, x, y)
            if abs(rx) > 1000000 or abs(ry) > 1000000:
                should_engrave = False
                break
        if should_engrave:
            ans += 1
            engrave[(x, y)] = True
    plot = ''
    lines = 0
    for x, y in coords:
        if (x, y) in engrave:
            plot += 'x'
        else:
            plot += '·'
        if (len(plot) - lines)%101 == 0:
            plot += '\n'
            lines += 1
    # print(plot)
    print(ans)


with open('3.in', 'r') as file:
    line = file.readline().strip()
    parts = line.split(',')
    x0 = int(parts[0].split('[')[-1])
    y0 = int(parts[1].split(']')[0])
    x1, y1 = add(x0, y0, 1000, 1000)
    coords = []
    for y in range(y0, y1+1):
        for x in range(x0, x1+1):
            coords.append((x, y))
    ans = 0
    engrave = {}
    for x, y in coords:
        should_engrave = True
        rx, ry = 0, 0
        for i in range(100):
            rx, ry = multiply(rx, ry, rx, ry)
            rx, ry = divide(rx, ry, 100000,100000)
            rx, ry = add(rx, ry, x, y)
            if abs(rx) > 1000000 or abs(ry) > 1000000:
                should_engrave = False
                break
        if should_engrave:
            ans += 1
            engrave[(x, y)] = True
    plot = ''
    lines = 0
    for x, y in coords:
        if (x, y) in engrave:
            plot += 'x'
        else:
            plot += '·'
        if (len(plot) - lines)%101 == 0:
            plot += '\n'
            lines += 1
    # print(plot)
    print(ans)

