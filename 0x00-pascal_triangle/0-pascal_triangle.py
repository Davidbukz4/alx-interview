#!/usr/bin/python3
'''
PASCAL TRIANGLE
'''


def pascal_triangle(n):
    ''' Returns a list of integers representing the pascal triangle'''
    res = []
    if n <= 0:
        return res
    for i in range(n+1):
        row = []
        coef = 1
        for j in range(1, i+1):
            row.append(coef)
            coef = (coef * (i - j)) // j
        if (len(row)):
            res.append(row)
    return res
