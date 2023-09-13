#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []

    for row in matrix:
        newRow = []

        for element in row:
            newRow.append(element ** 2)
        newMatrix.append(newRow)

    return newMatrix
