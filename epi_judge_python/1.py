from typing import List


def selection(list_):
    if list_:
        for i in range(len(list_) - 1):
            min_index = i
            for j in range(i + 1, len(list_)):
                if list_[j] < list_[min_index]:
                    min_index = j
            list_[i], list_[min_index] = list_[min_index], list_[i]


def insertion(list_):
    if list_:
        for i in range(1, len(list_)):
            insert_val = list_[i]
            j = i - 1
            while j >= 0 and list_[j] > insert_val:
                list_[j + 1] = list_[j]
                j -= 1
            list_[j + 1] = insert_val


def shell(list_):
    def gapinsertion(list_, start, interval):
        # in-place sort
        for i in range(start, len(list_), interval):
            j = i
            insert_val = list_[j]
            while j - interval >= start and insert_val < list_[j - interval]:
                list_[j] = list_[j - interval]
                j -= interval
            list_[j] = insert_val

    interval = len(list_) // 2
    while interval > 0:
        for i in range(interval):
            gapinsertion(list_, i, interval)
        interval >>= 1


def merge(list_):
    len_ = len(list_)
    if not list_:
        return None
    if len_ == 1:
        return list_
    else:
        middle = len_ // 2
        left_l = merge(list_[0:middle])
        upper_l = merge(list_[middle:])
        i, j = 0, 0
        res = []
        while i < len(left_l) and j < len(upper_l):
            if left_l[i] < upper_l[j]:
                res.append(left_l[i])
                i += 1
            else:
                res.append(upper_l[j])
                j += 1
        res.extend(left_l[i:] if j == len(upper_l) else upper_l[j:])
        return res


def quick(list_: List) -> None:
    from random import randint

    def _quick(list_: List, lower, upper):
        # 一定要设置 lower大于upper
        if lower >= upper:
            return
        lower_upper = lower
        pivot_idx = randint(lower, upper)
        pivot_val = list_[pivot_idx]
        list_[pivot_idx], list_[upper] = list_[upper], list_[pivot_idx]
        for i in range(lower, upper):
            if list_[i] < pivot_val:
                list_[i], list_[lower_upper] = list_[lower_upper], list_[i]
                lower_upper += 1
        list_[lower_upper], list_[upper] = list_[upper], list_[lower_upper]
        _quick(list_, lower, lower_upper - 1)
        _quick(list_, lower_upper + 1, upper)

    _quick(list_, 0, len(list_) - 1)


import itertools


def test(func, a):
    for p in itertools.permutations(a.copy()):
        p = list(p)
        # print(p)
        func(p)
        # print(p)
        assert a == p, 'algorithms fails'
    print('Test successful!')


a = [1, 2, 3, 4, 5, 6]
# a.reverse()
# print(a)
# quick(a)
# print(a)

test(quick, a)
