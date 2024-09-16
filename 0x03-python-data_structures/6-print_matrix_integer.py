#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    mat_len = len(matrix)
    mat_row = []
    for i in range(mat_len):
        mat_row = matrix[i]
        row_len = len(mat_row)
        for j in range(row_len):
            print("{:d}".format(mat_row[j]), end="")
            if j != row_len - 1:
                print(" ", end="")
        print()
