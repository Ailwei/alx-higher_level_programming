#!/usr/bin/python3

import numpy as np
""" function to multiply matrix"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): The first matrix to be multiplied.
        m_b (list of lists of int/float): The second matrix to be multiplied.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.

    Raises:
        ValueError: If m_a or m_b is not a list.
        ValueError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty.
        ValueError: If m_a and m_b cannot be multiplied.
        ValueError: If m_a and m_b should contain only integers or floats.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("m_a and m_b must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise ValueError("m_a and m_b must be lists of lists")

    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
        result = np.dot(np_m_a, np_m_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except Exception:
        raise ValueError("m_a and m_b should contain only integers or floats")
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
