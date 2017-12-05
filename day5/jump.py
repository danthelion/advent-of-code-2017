with open('input') as f:
    instructions = list(map(int, f.readlines()))

n = step = 0

while 0 <= n < len(instructions):
    if instructions[n] >= 3:  # PART 2
        instructions[n] -= 1
        n += instructions[n] + 1
    else:  # PART 1
        instructions[n] += 1
        n += instructions[n] - 1
    step += 1

print(step)
