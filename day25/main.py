steps = 12173597

a, b, c, d, e, f = range(6)

rules = {
    (a, 0): (1, 1, b),
    (a, 1): (0, 0, c),

    (b, 0): (1, 0, a),
    (b, 1): (1, 1, d),

    (c, 0): (1, 1, a),
    (c, 1): (0, 0, e),

    (d, 0): (0, 1, a),
    (d, 1): (1, 1, b),

    (e, 0): (1, 0, f),
    (e, 1): (1, 0, c),

    (f, 0): (1, 1, d),
    (f, 1): (1, 1, a)
}

tape = {}
head, state = 0, a

for i in range(steps):
    val = tape.get(head, 0)
    wval, move, nextstate = rules.get((state, val))

    tape[head] = wval
    head = head + 1 if move == 1 else head - 1
    state = nextstate

print(sum(tape.values()))
