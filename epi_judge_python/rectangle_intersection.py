import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # # TODO - you fill in here.
    # return Rect(0, 0, 0, 0)

    def is_intersect(r1,r2):
        return (r1.x<=r2.x+r2.width and r2.x<=r1.x+r1.width
                and r1.y<=r2.y+r2.height and r2.y<=r1.y+r1.height)
    def middle(x1,x2,x3,x4):
        s=sorted([x1,x2,x3,x4])
        return s[1],s[2]-s[1]

    if not is_intersect(r1,r2):
        return Rect(0, 0, -1, -1)
    x,x_w=middle(r1.x, r1.x + r1.width, r2.x, r2.x + r2.width)
    y, y_h = middle(r1.y, r1.y + r1.height, r2.y, r2.y + r2.height)
    return Rect(x,y,x_w,y_h)

def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
