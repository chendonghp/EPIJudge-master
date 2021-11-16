from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR=2
    def __init__(self, capacity: int) -> None:
        # TODO - you fill in here.
        self._queue=[None]*capacity
        self._front=0
        self._back=0
        self._num_ele=0

    #can increasing, can't decreasing
    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        # return
        if self._num_ele==len(self._queue):
            self._queue=self._queue[self._front:]+self._queue[:self._back]
            self._front,self._back=0,self._num_ele
            self._queue+=[None]*len(self._queue)*(self.SCALE_FACTOR-1)
        self._queue[self._back]=x
        self._back=(self._back+1)%len(self._queue)
        self._num_ele+=1

    def dequeue(self) -> int:
        # TODO - you fill in here.
        # return 0
        if not self._queue:
            raise IndexError('Empty Queue.')
        front=self._queue[self._front]
        self._front=(self._front+1)%len(self._queue)
        self._num_ele-=1
        return front

    def size(self) -> int:
        # TODO - you fill in here.
        # return 0
        return self._num_ele


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
