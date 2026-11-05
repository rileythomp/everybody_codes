def print_grid(grid):
    for row in grid:
        for v in row:
            print(v if v > 0 else '.', end='')
        print()


with open("1.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    grid = [[0 if x == '.' else int(x) for x in line] for line in lines]
    ans = 0
    ans_grid = []
    for i in range(len(grid)):
        ans_row = []
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                ans_row.append(0)
                continue
            if i == 0 or j == 0:
                ans += 1
                ans_row.append(grid[i][j])
                continue
            in_shadow = False
            for s in range(1, min(i, j) + 1):
                s_i = i-s
                s_j = j-s
                if 0 <= s_i < len(grid) and 0 <= s_j < len(grid[0]):
                    shadow_at_i_j = grid[s_i][s_j] - s
                    if grid[i][j] <= shadow_at_i_j:
                        ans_row.append(0)
                        break
            else:
                ans_row.append(grid[i][j])
                ans += 1
        ans_grid.append(ans_row)
    print(ans)

with open("2.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    grid = [[0 if x == '.' else int(x) for x in line] for line in lines]
    ans = 0
    for round_dir_i, round_dir_j in [(-1, -1), (1, 1), (-1, 1), (1, -1), (0, 1), (0, -1)]:
        ans_grid = []
        for i in range(len(grid)):
            ans_row = []
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    ans_row.append(0)
                    continue
                if (round_dir_i == -1 and i == 0) or (round_dir_i == 1 and i == len(grid)) or (round_dir_j == -1 and j == 0) or (round_dir_j == 1 and j == len(grid[0])):
                    ans += 1
                    ans_row.append(grid[i][j])
                    continue
                gap_size = 1 if round_dir_i != 0 else 2
                for s in range(gap_size, max(len(grid), len(grid[0])) + 1, gap_size):
                    s_i = i + (round_dir_i * s)
                    s_j = j + (round_dir_j * s)
                    if 0 <= s_i < len(grid) and 0 <= s_j < len(grid[0]):
                        shadow_at_i_j = grid[s_i][s_j] - s//gap_size
                        if grid[i][j] <= shadow_at_i_j:
                            ans_row.append(0)
                            break
                else:
                    ans_row.append(grid[i][j])
                    ans += 1
            ans_grid.append(ans_row)
    print(ans)
