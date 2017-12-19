# https://www.reddit.com/r/adventofcode/comments/7kr2ac/2017_day_19_solutions/drgk4ej/

with open('input') as f:
    lines = f.read().splitlines()

road = {x + 1j * y: v for y, line in enumerate(lines) for x, v in enumerate(line) if v.strip()}
direction, pos, path, dirs = 1j, min(road, key=lambda v: v.imag), [], [1j ** s for s in range(4)]
while pos in road:
    if road[pos] == '+':
        direction = next(d for d in dirs if pos + d in road and d != path[-1] - pos)
    path += [pos]
    pos += direction
print(''.join(c for c in map(road.get, path) if c.isalpha()))
print(len(path))
