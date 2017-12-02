# http://adventofcode.com/2017/day/1


def solve(captcha):
    digits_to_sum = []
    for i, e in enumerate(captcha):
        try:
            if e == captcha[i + (len(captcha) // 2)]:
                digits_to_sum.append(e)
        except IndexError:
            if e == captcha[i - (len(captcha) // 2)]:
                digits_to_sum.append(e)
    return sum(digits_to_sum)


if __name__ == '__main__':
    with open('input') as f:
        seq = list(map(int, f.read()))

    print(solve(seq))
