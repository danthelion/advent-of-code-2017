# http://adventofcode.com/2017/day/2


def calc_checksum(matrix):
    return sum([max(row) - min(row) for row in matrix])


if __name__ == '__main__':
    with open('input') as f:
        mx = [list(map(int, line.split('\t'))) for line in f.readlines()]

    print(calc_checksum(mx))
