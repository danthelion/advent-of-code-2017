# https://www.reddit.com/r/adventofcode/comments/7jpelc/2017_day_14_solutions/dr86te7/

from day10.main import solve2

data = 'hxtvlmkl'
rows = []

n = 0
for i in range(128):
    v = solve2('%s-%d' % (data, i))
    v = '{:0128b}'.format(int(v, 16))
    n += sum(list(map(int, v)))
    rows.append(list(map(int, v)))

print(n)

seen = set()
n = 0


def dfs(i, j):
    if ((i, j)) in seen:
        return
    if not rows[i][j]:
        return
    seen.add((i, j))
    if i > 0:
        dfs(i - 1, j)
    if j > 0:
        dfs(i, j - 1)
    if i < 127:
        dfs(i + 1, j)
    if j < 127:
        dfs(i, j + 1)


for i in range(128):
    for j in range(128):
        if (i, j) in seen:
            continue
        if not rows[i][j]:
            continue
        n += 1
        dfs(i, j)

print(n)
