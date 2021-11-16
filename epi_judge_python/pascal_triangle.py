from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    # return []
    pascal_tri=[]
    for i in range(1,n+1):
        row=[1]
        if i>2:
            for j in range(1,i-1):
                row.append(last_row[j-1]+last_row[j])
        if i>1:
            row.append(1)
        pascal_tri.append(row)
        last_row=row
    return pascal_tri


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
