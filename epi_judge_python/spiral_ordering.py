from typing import List

from test_framework import generic_test


# def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    # return []
    # l = len(square_matrix)
    # bound_length = l - 1
    # if l == 0:
    #     return []
    # if l == 1:
    #     return [square_matrix[0][0]]
    # spiral = []
    # i, j = 0, 0
    # while True:
    #     spiral.extend(square_matrix[i][j:j + bound_length])
    #     spiral.extend(list(zip(*square_matrix))[j + bound_length][i:i + bound_length])
    #     spiral.extend(square_matrix[i + bound_length][j + bound_length:j:-1])
    #     spiral.extend(list(zip(*square_matrix))[j][i + bound_length:i:-1])
    #     i += 1
    #     j += 1
    #     bound_length -= 2
    #     if bound_length == -1:
    #         return spiral
    #     if bound_length == 0:
    #         return spiral + [square_matrix[i][j]]

def matrix_in_spiral_order(square_matrix):
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix)) or next_y not in range(len(square_matrix)) or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x +SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
