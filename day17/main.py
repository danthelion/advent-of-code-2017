STEPS = 343

state = [0]
postition = 0
for i in range(2017):
    new = (postition + STEPS) % len(state)
    new += 1
    state.insert(new, i + 1)
    postition = new
print('Part 1:', state[postition + 1])

position = out = 0
cycle = 1
for i in range(50000000):
    insert = i + 1
    new = (position + STEPS) % cycle
    new += 1
    if new == 1:
        out = insert
    position = new
    cycle += 1
print('Part 2: ', out)
