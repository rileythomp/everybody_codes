with open('1.in', 'r') as f:
    data = f.read().strip()
    nums = [int(x) for x in data.split(',')]
    ans = 0
    for i in range(1, len(nums)):
        a, b = nums[i-1], nums[i]
        if abs(a-b) == 16:
            ans += 1
    print(ans)


with open('2.in', 'r') as f:
    data = f.read().strip()
    nums = [int(x) for x in data.split(',')]
    ans = 0
    edges = {n: [] for n in nums}
    for i in range(1, len(nums)):
        a, b = nums[i-1], nums[i]
        left, right = min(a, b), max(a, b)
        edges[left].append(right)
        edges[right].append(left)
        for i in range(left+1, right):
            nbrs = edges[i]
            for nbr in nbrs:
                if nbr < left or nbr > right:
                    ans += 1
    print(ans)


with open('3.in', 'r') as f:
    data = f.read().strip()
    nums = [int(x) for x in data.split(',')]
    ans = 0
    edges = {n: [] for n in nums}
    for i in range(1, len(nums)):
        a, b = nums[i-1], nums[i]
        left, right = min(a, b), max(a, b)
        edges[left].append(right)
        edges[right].append(left)
    upper = max(nums)
    for left in range(1, upper):
        for right in range(2, upper+1):
            score = 0
            if left in edges and right in edges[left]:
                score += 1
            for j in range(left+1, right):
                nbrs = edges[j] if j in edges else []
                for nbr in nbrs:
                    if nbr < left or nbr > right:
                        score += 1
            ans = max(ans, score)
    print(ans)
