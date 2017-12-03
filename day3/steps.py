def calc_distance(n):
    x = y = dx = step = 0
    dy = -1

    while True:
        step += 1
        if step == n:
            return abs(x) + abs(y)
        if (x == y) or (x > 0 and x == 1 - y) or (x < 0 and x == -y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


"""
part2 https://oeis.org/A141481 (369601)
"""

with open('input') as f:
    num = int(f.read())

print(calc_distance(num))
