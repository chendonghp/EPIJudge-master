from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # TODO - you fill in here.
    # return []
    decre_stack=[]
    index_stack=[]
    for i,s in enumerate(sequence):
        if not decre_stack:
            decre_stack.append(s)
            index_stack.append(i)
            continue
        else:
            while decre_stack and decre_stack[-1]<=s:
                decre_stack.pop()
                index_stack.pop()
        decre_stack.append(s)
        index_stack.append(i)
    index_stack.reverse()
    return index_stack

def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
