from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque
# class QueueWithMax:
#     def __init__(self):
#         self._queue=deque()
#         self._max_queue=deque()
#
#     def enqueue(self, x: int) -> None:
#         # TODO - you fill in here.
#         if self._max_queue:
#             if x >= self._max_queue[0]:
#                 self._max_queue.clear()
#             self._max_queue.append(x)
#         else:
#             self._max_queue.append(x)
#         self._queue.append(x)
#
#     def dequeue(self) -> int:
#         # TODO - you fill in here.
#         # return 0
#         if not self._queue:
#             raise IndexError('Queue is empty!')
#         elif self._max_queue[0] == self._queue[0]:
#             self._max_queue.popleft()
#             if self._max_queue:
#                 maxim = self._max_queue[0]
#                 maxim_index = 0
#                 for i, e in enumerate(self._max_queue):
#                     if e >= maxim:
#                         maxim=e
#                         maxim_index = i
#                 for _ in range(maxim_index):
#                     self._max_queue.popleft()
#         return self._queue.popleft()
#
#     def max(self) -> int:
#         # TODO - you fill in here.
#         if self._max_queue:
#             return self._max_queue[0]
#         else:
#             raise IndexError('Queue is empty!')


class QueueWithMax:
    def __init__(self):
        self._queue=deque()
        self._max_queue=deque()

    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        self._queue.append(x)
        while self._max_queue and x> self._max_queue[-1]:
            self._max_queue.pop()
        self._max_queue.append(x)

    def dequeue(self) -> int:
        # TODO - you fill in here.
        # return 0
        if self._queue:
            if self._queue[0]==self._max_queue[0]:
                self._max_queue.popleft()
            return self._queue.popleft()

    def max(self) -> int:
        # TODO - you fill in here.
        if self._max_queue:
            return self._max_queue[0]

def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
