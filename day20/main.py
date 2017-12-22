# https://www.reddit.com/r/adventofcode/comments/7kz6ik/2017_day_20_solutions/dricv8q/

import re
import collections

text = open("input").read().strip()
trans = str.maketrans("<>", "[]")
literal = re.sub(r'[^-\d,\<>\n]', '', text).translate(trans).splitlines()
particles = dict(enumerate(map(eval, literal)))
print(min(particles, key=lambda k: [x ** 2 + y ** 2 + z ** 2 for x, y, z in particles[k][::-1]]))

for tic in range(100):
    places = collections.defaultdict(set)
    for i, (p, v, a) in particles.items():
        places[tuple(p)].add(i)
        v = [x + y for x, y in zip(v, a)]
        p = [x + y for x, y in zip(p, v)]
        particles[i] = [p, v, a]
    collided = {i for g in places.values() for i in g if len(g) > 1}
    particles = {k: v for k, v in particles.items() if k not in collided}
print(len(particles))
