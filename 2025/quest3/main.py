with open("1.in", "r") as f:
    data = f.read().strip()
    nums = list(map(int, data.split(',')))
    seen = {}
    ans = 0
    for num in nums:
        if num not in seen:
            ans += num
            seen[num] = True
    print(ans)

with open("2.in", "r") as f:
    data = f.read().strip()
    nums = sorted(list(map(int, data.split(','))))
    seen = {}
    ans = 0
    for num in nums:
        if num not in seen:
            ans += num
            seen[num] = True
        if len(seen) == 20:
            break
    print(ans)

from collections import defaultdict

with open("3.in", "r") as f:
    data = f.read().strip()
    nums = sorted(list(map(int, data.split(','))))
    seen = defaultdict(int)
    for num in nums:
        seen[num] += 1
    print(max(seen.values()))
