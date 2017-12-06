import itertools
import sys

# yolo
sys.setrecursionlimit(10000)


def cycle(lst: list, c):
    max_bank_val = max(lst)
    max_bank_i = lst.index(max_bank_val)

    # Set max value to zero in list
    lst[max_bank_i] = 0

    cyc_i = itertools.cycle(range(len(lst)))

    extra_bank_counter = max_bank_val
    for i in itertools.islice(cyc_i, max_bank_i + 1, None):
        extra_bank_counter -= 1
        lst[i] += 1
        if extra_bank_counter == 0:
            break

    if tuple(lst) in seen:
        return c, seen

    seen[tuple(lst)] = c
    c += 1

    return cycle(lst, c)


with open('input') as f:
    banks = list(map(int, f.read().split('\t')))

count = 1
seen = {}

c, sx = cycle(banks, count)
# c = cycle([0, 2, 7, 0], count)

print(c)
print(c - sx[tuple(banks)])
