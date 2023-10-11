#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j] ** 2)
        new_matrix.append(row)

    return new_matrix
