with open("1.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    times = {}
    for line in lines:
        parts = line.split(' ')
        id = int(parts[0].split('=')[-1])
        time = int(parts[3].split('=')[-1])
        if id in times:
            times[id] += time
        else:
            times[id] = time
    times = sorted(times.values())
    ans = 0
    for i in range(len(times)):
        ans += (i+1)*times[i]

    print(ans)

from functools import cmp_to_key


def compare(a, b):
    parts_a, time_a = a
    parts_b, time_b = b
    if parts_a != parts_b:
        return parts_b - parts_a
    return time_a - time_b


with open("2.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    times = {}
    for line in lines:
        parts = line.split(' ')
        id = int(parts[0].split('=')[-1])
        time = int(parts[3].split('=')[-1])
        if id in times:
            times[id][1] += time
            times[id][0] += 1
        else:
            times[id] = [1, time]
    times = list(times.values())
    times.sort(key=cmp_to_key(compare))
    ans = 0
    for i in range(len(times)):
        parts, time = times[i]
        ans += (i+1)*time

    print(ans)


def compare2(a, b):
    id_a, time_a = a
    id_b, time_b = b
    return time_a - time_b

def parse_line(line):
    parts = line.split(' ')
    id = int(parts[0].split('=')[-1])
    quest = int(parts[1].split('=')[-1])
    part = int(parts[2].split('=')[-1])
    time = int(parts[3].split('=')[-1])
    return [id, quest, part, time]

from collections import defaultdict

times2 = defaultdict(lambda: defaultdict(dict))


with open("3.in", "r") as f:
    data = f.read().strip()
    lines = data.splitlines()
    lines = [parse_line(line) for line in lines]
    points = {}
    for id, quest, part, time in lines:
        times2[quest][part][id] = time
        points[id] = 0
    for quest, parts in times2.items():
        for part in [1, 2, 3]:
            times = parts[part]
            if part-1 in times2[quest]:
                for id, time in times2[quest][part-1].items():
                    if id in times2[quest][part]:
                        times2[quest][part][id] += time

    for quest, parts in times2.items():
        for part in  [1, 2, 3]:
            times = parts[part]
            times_list = [(id, time) for id, time in times.items()]
            times_list.sort(key=cmp_to_key(compare2))
            last_score = None
            last_time = None
            for i in range(len(times_list)):
                id, time = times_list[i]
                score = max(50*part - i, 0)
                if time == last_time:
                    score = last_score
                times_list[i] = (id, time, score)
                points[id] += score
                last_time = time
                last_score = score
    points = sorted(list(points.values()))[::-1]
    ans = 0
    last_points = None
    last_coeff = None
    for i in range(len(points)):
        coeff = i+1
        if points[i] == last_points:
            coeff = last_coeff
        ans += coeff*points[i]
        last_coeff = coeff
        last_points = points[i]
    print(ans)
