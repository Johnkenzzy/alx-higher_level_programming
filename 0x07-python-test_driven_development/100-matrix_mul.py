#!/usr/bin/python3
"""Definition of matrix_mul(m_a, m_b)
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list or list of lists.
        ValueError: If m_a or m_b are empty or can't be multiplied.
    """
    if m_a is None or type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if m_b is None or type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    row_size_a = len(m_a[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_size_b = len(m_b[0])
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            element_sum = 0
            for k in range(len(m_b)):
                element_sum += m_a[i][k] * m_b[k][j]
            row_result.append(element_sum)
        result.append(row_result)

    return result
