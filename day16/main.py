import re


def spin(l, pattern):
    spinning_slice = l[-int(pattern[1:]):]
    for _ in range(len(spinning_slice)):
        l.insert(0, l.pop(l.index(l[-1])))
    return l


def exchange(l, pattern):
    _pattern = re.compile('(\d+)/(\d+)')
    m = re.search(_pattern, pattern)
    a = int(m.group(1))
    b = int(m.group(2))
    l[a], l[b] = l[b], l[a]
    return l


def partner(l, pattern):
    _pattern = re.compile('([a-z])/([a-z])')
    m = re.search(_pattern, pattern)
    a = l.index(m.group(1))
    b = l.index(m.group(2))
    l[a], l[b] = l[b], l[a]
    return l


def do_move(l, pattern):
    spin_pattern = re.compile('^[a-z]\d+$')
    exchange_pattern = re.compile('^[a-z]\d+/\d+$')
    partner_pattern = re.compile('^[a-z][a-z]/[a-z]$')

    if spin_pattern.match(pattern):
        return spin(l, pattern)
    if exchange_pattern.match(pattern):
        return exchange(l, pattern)
    if partner_pattern.match(pattern):
        return partner(l, pattern)


def solve(p, m):
    for m in moves:
        p = do_move(programs, m)
    return p


with open("input") as f:
    moves = f.read().split(',')

# Part 1

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
seen = []
for _ in range(1):
    programs = solve(programs, moves)
    if tuple(programs) in seen:
        break
    seen.append(tuple(programs))

print('Part 1:', ''.join(programs))

# Part 2

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
seen = []
for _ in range(1000000000):
    programs = solve(programs, moves)
    p = ''.join(programs)
    if p in seen:
        print('Part 2:', ''.join(seen[(1000000000 % _) - 1]))
        break
    seen.append(p)


