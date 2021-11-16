from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    # def __init__(self):
    #     self.stack=[]
    #     self.max_n=None
    #
    # def empty(self) -> bool:
    #     # TODO - you fill in here.
    #     # return True
    #     return not self.stack
    #
    # def max(self) -> int:
    #     # TODO - you fill in here.
    #     # return 0
    #     return self.max_n
    #
    # def pop(self) -> int:
    #     # TODO - you fill in here.
    #     # return 0
    #     last_item=self.stack.pop()
    #     if self.stack:
    #         self.max_n=max(self.stack)
    #     return last_item
    #
    # def push(self, x: int) -> None:
    #     # TODO - you fill in here.
    #     # return
    #     self.stack.append(x)
    #     if self.stack:
    #         self.max_n=max(self.stack)
    from collections import namedtuple
    # element_with_max= namedtuple('element_with_max','element max')
    # def __init__(self):
    #     self._stacks=[]
    #
    # def empty(self) -> bool:
    #     return not self._stacks
    #
    # def max(self) -> int:
    #     if self._stacks:
    #         return self._stacks[-1].max
    #
    # def pop(self) -> int:
    #     if self._stacks:
    #         return self._stacks.pop().element
    #
    # def push(self, x: int) -> None:
    #     t_max=max(self._stacks[-1].max,x) if self._stacks else x
    #     self._stacks.append(self.element_with_max(x, t_max))

    class max_count:
        def __init__(self, max, count):
            self.max = max
            self.count = count

    def __init__(self):
        self._stacks = []
        self._max_stacks = []

    def empty(self) -> bool:
        return not self._stacks

    def max(self) -> int:
        if self._max_stacks:
            return self._max_stacks[-1].max

    def pop(self) -> int:
        if self._stacks:
            top = self._stacks.pop()
            if top == self._max_stacks[-1].max:
                self._max_stacks[-1].count -= 1
                if self._max_stacks[-1].count == 0:
                    self._max_stacks.pop()
            return top

    def push(self, x: int) -> None:
        self._stacks.append(x)
        if self._max_stacks:
            if self._max_stacks[-1].max < x:
                self._max_stacks.append(self.max_count(x, 1))
            elif self._max_stacks[-1].max == x:
                self._max_stacks[-1].count += 1
        else:
            self._max_stacks.append(self.max_count(x, 1))



def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
