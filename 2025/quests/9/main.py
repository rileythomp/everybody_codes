with open('1.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    dnas = {}
    childs = {}
    for line in lines:
        id, dna = line.split(':')
        dnas[int(id)] = dna
        childs[int(id)] = True

    for i in range(len(dnas[1])):
        letters = {}
        for id, dna in dnas.items():
            if dna[i] not in letters:
                letters[dna[i]] = [id]
            else:
                letters[dna[i]].append(id)
        for letters, ids in letters.items():
            if len(ids) == 1 and ids[0] in childs:
                del childs[ids[0]]
        if len(childs) == 1:
            break
    child = list(childs.keys())[0]
    child_dna = dnas[child]
    diffs = []
    for id, dna in dnas.items():
        diff = 0
        if id == child:
            continue
        for i in range(len(dna)):
            if dna[i] == child_dna[i]:
                diff += 1
        diffs.append(diff)
    ans = 1
    for diff in diffs:
        ans *= diff
    print(ans)




