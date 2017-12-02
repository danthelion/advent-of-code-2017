# http://adventofcode.com/2017/day/2


def find_evenly_dividing_nums(row):
    for num_1 in row:
        for num_2 in row:
            if num_1 % num_2 == 0 and num_1 != num_2:
                return num_1 // num_2


def calc_checksum(matrix):
    return sum([find_evenly_dividing_nums(row) for row in matrix])


if __name__ == '__main__':
    with open('input') as f:
        mx = [list(map(int, line.split('\t'))) for line in f.readlines()]

    print(calc_checksum(mx))
