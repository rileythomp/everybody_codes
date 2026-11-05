with open('1.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    graph = {}
    for line in lines:
        parts = line.split(':')
        left, right = parts[0], parts[1].split(',')
        graph[left] = right
    pop = 1
    dfs = [(0, 'A')]
    days = 4
    while len(dfs) > 0:
        depth, node = dfs.pop()
        nexts = graph[node]
        if depth + 1 <= days:
            pop -= 1
            for next in nexts:
                pop += 1
                dfs.append((depth+1, next))
    print(pop)

with open('2.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    graph = {}
    for line in lines:
        parts = line.split(':')
        left, right = parts[0], parts[1].split(',')
        graph[left] = right
    pop = 1
    dfs = [(0, 'Z')]
    days = 10
    while len(dfs) > 0:
        depth, node = dfs.pop()
        nexts = graph[node]
        if depth + 1 <= days:
            pop -= 1
            for next in nexts:
                pop += 1
                dfs.append((depth+1, next))
    print(pop)

with open('3.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    graph = {}
    for line in lines:
        parts = line.split(':')
        left, right = parts[0], parts[1].split(',')
        graph[left] = right
    pops = []
    max_pops = -1
    min_pops = 999999999
    for init in graph.keys():
        pop = 1
        dfs = [(0, init)]
        days = 20
        while len(dfs) > 0:
            depth, node = dfs.pop()
            if depth + 1 > days:
                continue
            nexts = graph[node]
            pop -= 1
            for next in nexts:
                pop += 1
                dfs.append((depth+1, next))
        pops.append(pop)
        max_pops = max(max_pops, pop)
        min_pops = min(min_pops, pop)
    print(max_pops - min_pops)
