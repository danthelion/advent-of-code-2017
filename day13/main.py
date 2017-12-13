# https://www.reddit.com/r/adventofcode/comments/7jgyrt/2017_day_13_solutions/dr6bug2/

d = {}
with open("input") as maf:
    for line in maf:
        l = line.strip().split(": ")
        d[int(l[0])] = int(l[1])

j = len(d)

s = 0
for i in d.keys():
    k = d[i]
    if i % (2 * k - 2) == 0:
        s += i * k

print(s)

de = 0
ok = False
while not ok:
    ok = True
    for i in d.keys():
        k = d[i]
        if (i + de) % (2 * k - 2) == 0:
            ok = False
            de += 1
            break

print(de)
