from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self):
        self._queue=[]
        self._dequeue=[]

    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        # return
        self._queue.append(x)

    def dequeue(self) -> int:
        # TODO - you fill in here.
        # return 0
        if not self._dequeue:
            while self._queue:
                self._dequeue.append(self._queue.pop())
        if not self._dequeue:
            raise IndexError('Queue is empty!')
        return self._dequeue.pop()

def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
