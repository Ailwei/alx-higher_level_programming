#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiply two matrices, m_a and m_b.

    Args:
        m_a (list of lists): The first matrix represented as a list of lists.
        m_b (list of lists): The second matrix represented as a list of lists.

    Returns:
        list of lists: The product of the two input matrices.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, contains non-integer or non-float elements,
                   or has rows of different sizes.
        ValueError: If m_a or m_b is empty or cannot be multiplied.

    The function performs matrix multiplication by validating the input matrices and
    then calculating the product if they meet the necessary conditions.

    Note: Matrix multiplication is only defined when the number of columns in m_a
    is equal to the number of rows in m_b.

    Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    """
    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    
    if not all(isinstance(val, (int, float)) for row in m_a for val in row) or not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
