with open('1.in', 'r') as f:
    data = f.read().strip()
    swords = [x for x in data if x in ['a', 'A']]
    caps_seen = 0
    ans = 0
    for sword in swords:
        if sword == 'a':
            ans += caps_seen
        else:
            caps_seen += 1
    print(ans)

def calc(letters):
    caps_seen = 0
    ans = 0
    for letter in letters:
        if letter == letters[0].lower():
            ans += caps_seen
        else:
            caps_seen += 1
    return ans

with open('2.in', 'r') as f:
    data = f.read().strip()
    print(sum([calc([l for l in data if l in [letter, letter.upper()]]) for letter in 'abc']))

from collections import defaultdict

with open('3.in', 'r') as f:
    data = f.read().strip()
    repeats = 1000
    window_size = 1000
    people = data*repeats
    prev_start, prev_end = max(0, 0-window_size), min(0+window_size, len(people)-1)
    cur_window_counts = defaultdict(int)
    for i in range(prev_start, prev_end+1):
        if people[i] in 'ABC':
            cur_window_counts[people[i]] += 1
    ans = 0
    for i in range(len(people)):
        person = people[i]
        cur_start, cur_end = max(0, i-window_size), min(i+window_size, len(people)-1)
        if cur_end != prev_end:
            if people[cur_end] in 'ABC':
                cur_window_counts[people[cur_end]] += 1
        if cur_start != prev_start:
            if people[prev_start] in 'ABC':
                cur_window_counts[people[prev_start]] -= 1
        if person in 'abc':
            ans += cur_window_counts[person.upper()]
        prev_start, prev_end = cur_start, cur_end
    print(ans)
