def satisfies(name, rules_follow):
    for i in range(1, len(name)):
        left, right = name[i-1], name[i]
        if left not in rules_follow or right not in rules_follow[left]:
            return False
    return True

with open('1.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    names = lines[0].split(',')
    rule_strs = lines[2:]
    rules_follow = {}
    for rule_str in rule_strs:
        left, right = rule_str.split(' > ')
        follows = right.split(',')
        rules_follow[left] = follows
    ans = ''
    for name in names:
        if satisfies(name, rules_follow):
            ans = name
    print(ans)


with open('2.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    names = lines[0].split(',')
    rule_strs = lines[2:]
    rules_follow = {}
    for rule_str in rule_strs:
        left, right = rule_str.split(' > ')
        follows = right.split(',')
        rules_follow[left] = follows
    ans = 0
    for i in range(len(names)):
        name = names[i]
        if satisfies(name, rules_follow):
            ans += i+1
    print(ans)

with open('3.in', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')
    names = lines[0].split(',')
    rule_strs = lines[2:]
    rules_follow = {}
    rules_precede = {}
    for rule_str in rule_strs:
        left, right = rule_str.split(' > ')
        follows = right.split(',')
        rules_follow[left] = follows
        for follow in follows:
            if follow in rules_precede:
                rules_precede[follow].append(left)
            else:
                rules_precede[follow] = [left]
    seen = {}
    for i in range(len(names)):
        name = names[i]
        if not satisfies(name, rules_follow):
            continue
        dfs = [name]
        while len(dfs) > 0:
            cur_name = dfs.pop()
            if cur_name not in seen and len(cur_name) >= 7 and len(cur_name) <= 11:
                seen[cur_name] = True
            if len(cur_name) == 11:
                continue
            last_letter = cur_name[-1]
            if last_letter not in rules_follow:
                continue
            follows = rules_follow[last_letter]
            for follow in follows:
                dfs.append(cur_name + follow)
    print(len(seen))
