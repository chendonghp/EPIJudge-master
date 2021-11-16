from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    # TODO - you fill in here.
    # return []
    max_heap=[]#left
    min_heap=[]
    result=[]
    import heapq
    for s in sequence:
        heapq.heappush(min_heap,-heapq.heappushpop(max_heap,-s))
        if len(min_heap)>len(max_heap)+1:
            heapq.heappush(max_heap,-heapq.heappop(min_heap))
            result.append(0.5*(min_heap[0]-max_heap[0]))
        else:
            result.append(min_heap[0])
    return result



def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
