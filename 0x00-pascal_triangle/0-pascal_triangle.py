#!/usr/bin/python3
'''
PASCAL TRIANGLE
'''


def pascal_triangle(n):
    '''
    Returns a list of integers representing the pascal triangle for n rows
    '''
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        row_list = []
        for k in range(row + 1):
            coef = factorial(row) // (factorial(k) * factorial(row - k))
            row_list.append(coef)
        triangle.append(row_list)
    return triangle


def factorial(n):
    ''' Returns the factorial of a number '''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
