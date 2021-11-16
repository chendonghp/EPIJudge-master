from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    #book
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

    ## mine, use recursion, two time cost compare with book
    # if y<0:
    #     x = 1/x
    #     y=-y
    # if y == 0:
    #     return 1
    # if y & 1:
    #     return power(x, y-1) * x
    # else:
    #     return power(x, y>>1) **2
    # return 0.0

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
