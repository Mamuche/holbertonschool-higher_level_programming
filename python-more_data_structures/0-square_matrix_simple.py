#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[1]] * len(matrix)
    i_index = 0
    for i in matrix:
        new_matrix[i_index] = [x**2 for x in i]
        i_index += 1
    return (new_matrix)
