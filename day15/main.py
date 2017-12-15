def generate(n, f, m=1):
    while True:
        n = n * f % 2147483647
        if n % m == 0:
            yield n


# Part 1
gen_a, gen_b = generate(116, 16807), generate(299, 48271)

total = 0

for _ in range(40000000):
    a = next(gen_a)
    b = next(gen_b)
    if a % 65536 == b % 65536:
        total += 1


print('Part 1:', total)

# Part 2
gen_a, gen_b = generate(116, 16807, 4), generate(299, 48271, 8)

total = 0

for _ in range(5000000):
    a = next(gen_a)
    b = next(gen_b)
    if a % 65536 == b % 65536:
        total += 1


print('Part 2:', total)
