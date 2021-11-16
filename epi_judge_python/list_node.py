class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


    def __eq__(self, other):
        a, b = self, other
        while a and b:
            if a.data != b.data:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def __repr__(self):
        node = self
        visited = set()
        first = True

        result = ''

        while node:
            if first:
                first = False
            else:
                result += ' -> '

            if id(node) in visited:
                if node.next is not node:
                    result += str(node.data)
                    result += ' -> ... -> '

                result += str(node.data)
                result += ' -> ...'
                break
            else:
                result += str(node.data)
                visited.add(id(node))
            node = node.next

        return result

    def __str__(self):
        return self.__repr__()


def list_size(node):
    result = 0
    visited = set()

    while node is not None and id(node) not in visited:
        result += 1
        visited.add(id(node))
        node = node.next

    return result


class SLList:
    #singly_linked_list
    def __init__(self,l:list):
        self.head=None
        for e in reversed(l):
            self.head=ListNode(e,self.head)
        self.list=self.head

    def __repr__(self):
        return str(self.head)

