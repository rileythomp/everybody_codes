with open("1.in", "r") as f:
    data = f.read().strip()
    nums = list(map(int, data.split(',')))
    ans = 0
    for num in nums:
        if int(num ** 0.5) != num**0.5:
            a = (int(num ** 0.5)+1)**2
            ans += (a - num)

    print(ans)

with open('2.in', 'r') as f:
    data = f.read().strip()
    nums = list(map(int, data.split(',')))
    ans = 0
    for num in nums:
        if num < 8:
            ans += (8 - num)
            continue
        if int(num/4 + 1) != num/4 + 1:
            p = 4*int(num/4 + 1)
            ans += (p - num)

    print(ans)

with open("3.in", "r") as f:
    data = f.read().strip()
    nums = list(map(int, data.split(',')))
    ans = 0
    for num in nums:
        if num <= 8:
            ans += (8 - num)
            continue
        s = int(num**0.5) + 1
        if s%2 == 0:
            s += 1
        p = s**2 - 1
        ans += (p - num)
        # if int(num ** 0.5) != num**0.5:
        #     a = (int(num ** 0.5)+1)**2
        #     ans += (a - num)

    print(ans)


    # 3 8
    # 5 24
    # 7 48
    # 9 80
    # p = n**2 - 1

    # 23 -> 4.79 -> 5 -> 24 -> (24-23) -> 1
    # 24 -> 4.48 -> 5 -> 24 -> (24-24) -> 0
    # 25 -> 5.00 -> 7 -> 48 -> (48-25) -> 23

    # 35 -> 5.91 -> 7 -> 48 -> (48-35) -> 13
    # 36 -> 6.00 -> 7 -> 48 -> (48-36) -> 12

    # 47 -> 6.85 -> 7 -> 48 -> (48-47) -> 1
    # 48 -> 6.92 -> 7 -> 48 -> (48-48) -> 0
    # 49 -> 7.00 -> 9 -> 80 -> (80-49) -> 31
