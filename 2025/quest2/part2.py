def multiply(x1, y1, x2, y2):
    return x1 * x2 - y1 * y2, x1 * y2 + y1 * x2

def divide(x1, y1, x2, y2):
    return x1 // x2, y1 // y2

def add(x1, y1, x2, y2):
    return x1 + x2, y1 + y2

grid = []

with open('part2.txt', 'r') as file:
    line = file.readline().strip()
    parts = line.split(',')
    topx = int(parts[0].split('[')[-1])
    topy = int(parts[1].split(']')[0])
    bottomx, bottomy = add(topx, topy, 1000, 1000)
    px, py = topx, topy
    engrave = 0
    p = 0
    while py <= bottomy:
        row = []
        while px <= bottomx:
            p += 1
            rx, ry = 0, 0
            broke = False
            for i in range(100):
                rx, ry = multiply(rx, ry, rx, ry)
                rx, ry = divide(rx, ry, 100000, 100000)
                rx, ry = add(rx, ry, px, py)
                if px == 35630 and py == -64880:
                    print(f'i={i}, P=[{px},{py}]   R=[{rx},{ry}], engraved?={not broke}')
                if abs(rx) > 1000000 or abs(ry) > 1000000:
                    broke = True
                    break
            if not broke:
                row.append('x')
                engrave += 1
            else:
                row.append('·')
            if px == 35630 and py == -64880:
                print(f'P=[{px},{py}]   R=[{rx},{ry}], engraved?={not broke}')
            # if px == 35630 and py == -64870:
            #     print(f'P=[{px},{py}]   R=[{rx},{ry}], engraved?={not broke}')
            # if px == 35640 and py == -64860:
            #     print(f'P=[{px},{py}]   R=[{rx},{ry}], engraved?={not broke}')
            # if px == 36230 and py == -64270:
            #     print(f'P=[{px},{py}]   R=[{rx},{ry}], engraved?={not broke}')
            # if px == 36250 and py == -64270:
            #     print(f'P=[{px},{py}]   R=[{rx},{ry}], engraved?={not broke}')
            px += 10
        grid.append(''.join(row))
        py += 10
        px = topx
    # print(engrave)
    # for line in grid:
    #     print(line)
