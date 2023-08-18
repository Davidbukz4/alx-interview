#!/usr/bin/python3
'''
Rotate 2D Matrix
'''


def rotate_2d_matrix(matrix):
    ''' rotates an n x n matrix 90 degrees clockwise '''
    # transpose the matrix
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse the rows
    for row in matrix:
        row.reverse()
