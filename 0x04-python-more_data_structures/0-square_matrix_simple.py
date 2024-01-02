#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []

    for row in matrix:
        squared_row = []

        for element in row:
            squared_value = element ** 2
            squared_row.append(squared_value)

        squared_matrix.append(squared_row)

    return squared_matrix
