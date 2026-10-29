def multiply(x1, y1, x2, y2):
    return x1 * x2 - y1 * y2, x1 * y2 + y1 * x2

def divide(x1, y1, x2, y2):
    return x1 // x2, y1 // y2

def add(x1, y1, x2, y2):
    return x1 + x2, y1 + y2

with open('part1.txt', 'r') as file:
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
