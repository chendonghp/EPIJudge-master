from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:

    # Generate all subsets whose intersection with input_set[0], ...,
    # input_set[to_be_selected - 1] is exactly selected_so_far.
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(selected_so_far)
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        # Generate all subsets that contain input_set[to_be_selected].
        directed_power_set(to_be_selected + 1,
                           selected_so_far + [input_set[to_be_selected]])

    power_set: List[List[int]] = []
    directed_power_set(0, [])
    return power_set


# Pythonic solution
def generate_power_set_pythonic(S):
    power_set = [[]]
    for a in S:
        power_set += [s + [a] for s in power_set]
        # # 一个奇怪的的特性，下面这种写法会产生无穷循环，power_set一直在增加
        # for s in power_set:
        #     power_set += [s + [a]]
        # # 下面的方法可以解决, 使用copy, list comprehension似乎也是用了这种方式
        # for s in power_set.copy():
        #     power_set += [s + [a]]
    return power_set

    #


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
