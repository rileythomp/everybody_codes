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
    ans2 = 0
    ans_grid = []
    for i in range(len(grid)):
        ans_row = []
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                ans_row.append(0)
                continue
            if i == 0 or j == 0:
                ans += grid[i][j]
                ans2 += 1
                ans_row.append(grid[i][j])
                continue
            max_shadow = 0
            in_shadow = False
            for s in range(1, min(i, j) + 1):
                s_i = i-s
                s_j = j-s
                if 0 <= s_i < len(grid) and 0 <= s_j < len(grid[0]):
                    shadow_at_i_j = grid[s_i][s_j] - s
                    if grid[i][j] <= shadow_at_i_j:
                        in_shadow = True
            if not in_shadow:
                ans_row.append(grid[i][j])
                ans += grid[i][j]
                ans2 += 1
            else:
                ans_row.append(0)
        ans_grid.append(ans_row)
    print(ans2)

with open("2.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    grid = [[0 if x == '.' else int(x) for x in line] for line in lines]
    rounds = [(-1, -1), (1, 1), (-1, 1), (1, -1), (0, 1), (0, -1)]#, (0, -1)]
    p2 = 0
    for round in rounds:
        round_dir_i, round_dir_j = round
        ans = 0
        ans2 = 0
        ans_grid = []
        for i in range(len(grid)):
            ans_row = []
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    ans_row.append(0)
                    continue
                # check might need to include i and j == len grid
                if (round == (-1, -1)) and (i == 0 or j == 0):
                    ans += grid[i][j]
                    ans2 += 1
                    ans_row.append(grid[i][j])
                    continue
                elif (round == (1, 1)) and (i == len(grid)-1 or j == len(grid[0])-1):
                    ans += grid[i][j]
                    ans2 += 1
                    ans_row.append(grid[i][j])
                    continue
                elif (round == (-1, 1)) and (i == 0 or j == len(grid[0])-1):
                    ans += grid[i][j]
                    ans2 += 1
                    ans_row.append(grid[i][j])
                    continue
                elif (round == (1, -1)) and (i == len(grid)-1 or j == 0):
                    ans += grid[i][j]
                    ans2 += 1
                    ans_row.append(grid[i][j])
                    continue
                elif (round == (0, -1)) and (j == 0):
                    ans += grid[i][j]
                    ans2 += 1
                    ans_row.append(grid[i][j])
                    continue
                elif (round == (0, 1)) and (j == len(grid[0])-1):
                    ans += grid[i][j]
                    ans2 += 1
                    ans_row.append(grid[i][j])
                    continue
                max_shadow = 0
                in_shadow = False
                # might need to change bound here
                s_upper_bound = None
                if round == (-1, -1):
                    s_upper_bound = max(i, j) + 1
                elif round == (1, 1):
                    s_upper_bound = max(i, j) + 1
                elif round == (-1, 1):
                    s_upper_bound = max(i, j) + 1
                elif round == (1, -1):
                    s_upper_bound = max(i, j) + 1
                elif round == (0, -1):
                    s_upper_bound = len(grid[0]) + 1
                elif round == (0, 1):
                    s_upper_bound = len(grid[0]) + 1

                if round_dir_i != 0:
                    for s in range(1, s_upper_bound):
                        # will need to change the subtraction/addition here
                        # s_i = i - s
                        # s_j = j - s
                        s_i = i + (round_dir_i * s)
                        s_j = j + (round_dir_j * s)
                        if 0 <= s_i < len(grid) and 0 <= s_j < len(grid[0]):
                            shadow_at_i_j = grid[s_i][s_j] - s
                            if grid[i][j] <= shadow_at_i_j:
                                in_shadow = True
                else:
                    for s in range(2, s_upper_bound, 2):
                        s_i = i + (round_dir_i * s)
                        s_j = j + (round_dir_j * s)
                        if 0 <= s_i < len(grid) and 0 <= s_j < len(grid[0]):
                            shadow_at_i_j = grid[s_i][s_j] - s//2
                            if grid[i][j] <= shadow_at_i_j:
                                in_shadow = True
                if not in_shadow:
                    ans_row.append(grid[i][j])
                    ans += grid[i][j]
                    ans2 += 1
                else:
                    ans_row.append(0)
            ans_grid.append(ans_row)
        p2 += ans2
    print(p2)
