with open("1.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    ans = 0
    for line in lines:
        pairs = line.split()
        num_counts = {n: 0 for n in range(1, 6)}
        for pair in pairs:
            left = int(pair[0])
            right = int(pair[2])
            cmp = pair[1]
            if cmp == '<':
                num_counts[right] += 1
            else:
                num_counts[left] += 1
        for num, count in num_counts.items():
            ans += (num*(10**count))
    print(ans)

with open("2.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    ans = 0
    for line in lines:
        line_ans = 0
        pairs = line.split()
        num_counts = {n: 0 for n in range(1, 10)}
        outbound_nodes = {}
        for pair in pairs:
            left = int(pair[0])
            right = int(pair[2])
            cmp = pair[1]
            if cmp == '<':
                num_counts[right] += 1
                outbound_nodes[left] = right
            else:
                num_counts[left] += 1
                outbound_nodes[right] = left
        count_nums = {}
        for num, count in num_counts.items():
            if count in count_nums:
                existing_num = count_nums[count][0]
                # undo the initial add
                ans -= (existing_num*(10**count))
                if num in outbound_nodes:
                    ans += (num*(10**count))
                    ans += (existing_num*(10**(count+1)))
                elif existing_num in outbound_nodes:
                    ans += (num*(10**(count+1)))
                    ans += (existing_num*(10**count))
                count_nums[count].append(num)
            else:
                # add the number
                ans += (num*(10**count))
                count_nums[count] = [num]
    print(ans)

with open("3.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    ans = 0
    for line in lines:
        line_ans = 0
        pairs = line.split()
        num_nodes = 0
        for pair in pairs:
            num_nodes = max(num_nodes, int(pair[0]), int(pair[2]))
        outbound_nodes = {str(n): [] for n in range(1, num_nodes+1)}
        inbound_nodes = {str(n): [] for n in range(1, num_nodes+1)}
        for pair in pairs:
            left = pair[0]
            right = pair[2]
            cmp = pair[1]
            if cmp == '<':
                outbound_nodes[left].append(right)
                inbound_nodes[right].append(left)
            else:
                outbound_nodes[right].append(left)
                inbound_nodes[left].append(right)
        dfs = []
        for node, outbound in outbound_nodes.items():
            if len(outbound) == 0:
                dfs = [[node]]
        while len(dfs) > 0:
            cur_path = dfs.pop()
            if len(cur_path) == num_nodes:
                ans += int(''.join(cur_path))
                break
            inbound = inbound_nodes[cur_path[-1]]
            for node in inbound:
                dfs.append(cur_path + [node])
    print(ans)

