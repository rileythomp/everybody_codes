# (dx_i, dx_j)
nexts = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

with open('1.in', 'r') as f:
    data = f.read().strip()
    grid = [list(row) for row in data.split('\n')]
    d_i, d_j = 0, 0
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == 'D':
                d_i, d_j = i, j
    seen = {}
    bfs = [(0, d_i, d_j)]
    ans = 0
    rounds = 4
    while len(bfs) > 0:
        cur_round, cur_i, cur_j = bfs.pop(0)
        if grid[cur_i][cur_j] == 'S' and (cur_i, cur_j) not in seen:
            ans += 1
        seen[(cur_i, cur_j)] = True
        for dx_i, dx_j in nexts:
            next_i, next_j = cur_i + dx_i, cur_j + dx_j
            if cur_round + 1 <= rounds and 0 <= next_i < len(grid) and 0 <= next_j <= len(grid[0]):
                bfs.append((cur_round+1, next_i, next_j))
    print(ans)

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

with open('2.in', 'r') as f:
    data = f.read().strip()
    grid = [list(row) for row in data.split('\n')]
    d_i, d_j = 0, 0
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == 'D':
                d_i, d_j = i, j
    sheep = []
    for row in grid:
        sheep_row = []
        for elem in row:
            if elem in 'D#':
                sheep_row.append('.')
            else:
                sheep_row.append(elem)
        sheep.append(sheep_row)
    hideouts = []
    for row in grid:
        hideout_row = []
        for elem in row:
            if elem in 'DS':
                hideout_row.append('.')
            else:
                hideout_row.append(elem)
        hideouts.append(hideout_row)
    dragons = {}
    bfs = [(0, d_i, d_j)]
    ans = 0
    rounds = 20
    while len(bfs) > 0:
        cur_round, cur_i, cur_j = bfs.pop()
        if cur_round > 0 and cur_round not in dragons:
            dragons[cur_round] = {(cur_i, cur_j)}
        elif cur_round in dragons:
            dragons[cur_round].add((cur_i, cur_j))

        for dx_i, dx_j in nexts:
            next_i, next_j = cur_i + dx_i, cur_j + dx_j
            if cur_round + 1 <= rounds and 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) \
                and (cur_round+1 not in dragons or ((next_i, next_j) not in dragons[cur_round+1])):
                bfs.append((cur_round+1, next_i, next_j))
    for round in sorted(dragons.keys()):
        places = dragons[round]
        for i, j in places:
            if sheep[i][j] == 'S' and hideouts[i][j] != '#':
                ans += 1
                sheep[i][j] = '.'
        sheep = [['.' for _ in range(len(sheep[0]))]] + sheep[0:-1]
        for i, j in places:
            if sheep[i][j] == 'S' and hideouts[i][j] != '#':
                ans += 1
                sheep[i][j] = '.'
    print(ans)
