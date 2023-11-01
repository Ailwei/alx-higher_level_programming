#!/usr/bin/python3
"""matrix function"""

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists of int/float): The first matrix to be multiplied.
        m_b (list of lists of int/float): The second matrix to be multiplied.

    Returns:
        A new matrix representing the result of the multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty (i.e., [] or [[]]).
        TypeError: If an element in m_a or m_b is not an integer or float.
        TypeError: If the rows in m_a or m_b are not of the same size.
        ValueError: If m_a and m_b cannot be multiplied.
        """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_1 = []
    for i in range(len(m_b[0])):
        my_row = []
        for j in range(len(m_b)):
            my_row.append(m_b[j][i])
        matrix_1.append(my_row)

    matrix_2 = []
    for row in m_a:
        my_row = []
        for column in matrix1:
            product = 0
            for m in range(len(matrix_1[0])):
                product += row[m] * column[m]
            my_row.append(product)
        matrix_2.append(my_row)

    return matrix_2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
