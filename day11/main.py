with open('input') as f:
    directions = f.readline().split(',')

x = y = z = 0

distances = []

for d in directions:
    if d == "n":
        y += 1
        z -= 1
    elif d == "s":
        y -= 1
        z += 1
    elif d == "ne":
        x += 1
        z -= 1
    elif d == "sw":
        x -= 1
        z += 1
    elif d == "nw":
        x -= 1
        y += 1
    elif d == "se":
        x += 1
        y -= 1
    _distance = (abs(x) + abs(y) + abs(z)) // 2
    distances.append(_distance)

print('1', (abs(x) + abs(y) + abs(z)) // 2)
print('2', max(distances))
