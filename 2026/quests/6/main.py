with open("1.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    graph = {}
    for line in lines:
        left = line.split(':')[0]
        right = line.split(':')[1].split(',')
        graph[left] = right
    dfs = ['NULL']
    seen = set()
    while len(dfs) > 0:
        cur = dfs.pop()
        seen.add(cur)
        if cur not in graph: continue
        nbrs = graph[cur]
        for nbr in nbrs:
            if nbr not in seen:
                dfs.append(nbr)
    print(len(seen)-1)

with open("2.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    graph = {}
    for line in lines:
        left = line.split(':')[0]
        right = line.split(':')[1].split(',')
        graph[left] = right
    ans = 0
    for node in graph.keys():
        if node == 'NULL': continue
        dfs = [node]
        seen = set()
        while len(dfs) > 0:
            cur = dfs.pop()
            seen.add(cur)
            if cur not in graph: continue
            nbrs = graph[cur]
            for nbr in nbrs:
                if nbr not in seen:
                    dfs.append(nbr)
        if 'NULL' in seen:
            ans += 1
    print(ans)

with open("3.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    graph = {}
    for line in lines:
        left = line.split(':')[0]
        right = line.split(':')[1].split(',')
        graph[left] = right
    ans = 0
    for node in graph.keys():
        if node in ('NULLv1', 'NULLv2', 'NULLv3'): continue
        dfs = [node]
        seen = set()
        while len(dfs) > 0:
            cur = dfs.pop()
            seen.add(cur)
            if cur not in graph: continue
            nbrs = graph[cur]
            for nbr in nbrs:
                if nbr not in seen:
                    dfs.append(nbr)
        if ('NULLv1' in seen and 'NULLv2' in seen) or ('NULLv1' in seen and 'NULLv3' in seen) or ('NULLv2' in seen and 'NULLv3' in seen):
            ans += 1
    print(ans)
