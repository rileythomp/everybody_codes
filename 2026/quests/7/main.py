with open("1.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    graph = {}
    for line in lines:
        id = int(line.split(', ')[0].split('=')[-1])
        energy = int(line.split(', ')[1].split('=')[-1])
        connections = [int(x) for x in line.split(', ')[2].split('=')[-1].split(',')]
        graph[id] = (energy, connections)

    most_conns_id = -1
    most_conns = -1
    ans = 0
    for id in graph.keys():
        energy, conns = graph[id]
        ans += energy
        if len(conns) > most_conns:
            most_conns_id = id
            most_conns = len(conns)
    # print(most_conns_id)
    bfs = [(5, most_conns_id)]
    while len(bfs) > 0:
        depth, cur_id = bfs.pop(0)
        ans += depth
        energy, conns = graph[cur_id]
        for conn in conns:
            if depth-1 > 0:
                bfs.append((depth-1, conn))
    print(ans)

from collections import deque

with open("2.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    graph = {}
    for line in lines:
        id = int(line.split(', ')[0].split('=')[-1])
        energy = int(line.split(', ')[1].split('=')[-1])
        connections = [int(x) for x in line.split(', ')[2].split('=')[-1].split(',')]
        graph[id] = (energy, connections)

    most_conns_id = -1
    most_conns = -1
    ans = 0
    for id in graph.keys():
        energy, conns = graph[id]
        ans += energy
        if len(conns) > most_conns:
            most_conns_id = id
            most_conns = len(conns)
    # print(most_conns_id)
    # bfs = [(10, most_conns_id)]
    bfs = deque()
    bfs.append((10, most_conns_id))
    while len(bfs) > 0:
        depth, cur_id = bfs.popleft()
        ans += depth
        energy, conns = graph[cur_id]
        for conn in conns:
            if depth-1 > 0:
                bfs.append((depth-1, conn))
    print(ans)
