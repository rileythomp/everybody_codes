def calc(line):
    ans = 0
    parts = line.split(' ')
    bases, coeffs = parts[0].split('-')[-1], parts[1]
    for n in range(len(bases)):
        ans += (int(coeffs[n]))*(int(bases[n])**(len(bases)-1-n))
    return ans

with open("1.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    ans = 0
    for line in lines:
        ans += calc(line)
    print(ans)

def calc2(line):
    ans = 0
    parts = line.split(' ')
    bases, coeffs = parts[0].split('-')[-1], parts[1]
    for i in range(len(coeffs)):
        coeff = int(coeffs[::-1][i])
        base = int(bases[::-1][i%len(bases)])
        ans += coeff*(base**(i))
    return ans

with open("2.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    ans = 0
    for line in lines:
        ans += calc2(line)
    print(ans)

def calc3(line):
    ans = 0
    parts = line.split(' ')
    bases, coeffs = parts[0].split('-')[-1], parts[1]
    for i in range(len(coeffs)):
        coeff = int(coeffs[::-1][i])
        base = int(bases[::-1][i%len(bases)])
        ans += coeff*(base**i)
    smallest = True
    for next_coeff in range(int(coeffs)-1, 0, -1):
        next_ans = 0
        for i in range(len(str(next_coeff))):
            coeff = int(str(next_coeff)[::-1][i])
            base = int(bases[::-1][i%len(bases)])
            next_ans += coeff*(base**i)
        if next_ans == ans:
            smallest = False
            break
    return ans if smallest else 0

with open("3.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    ans = 0
    for line in lines:
        ans += calc3(line)
    print(ans)
