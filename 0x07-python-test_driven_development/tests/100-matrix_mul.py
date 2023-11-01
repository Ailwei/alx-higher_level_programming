import doctest
from matrix_mul import matrix_mul

def test_matrix_mul():
    """
    Test cases for the matrix_mul function.
    
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
    
    >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    [[13, 16]]
    
    >>> matrix_mul([[1.2, 5.5, 6.2], [4.66, 12.3, -9.2]], [[5.0, 3.3], [-2.9, 4.4], [7.2, 4.4]])
    [[34.69, 55.44000000000001], [-78.61, 29.018000000000008]]
    
    >>> matrix_mul([[1,2]], [[3,4], [5,6], [7, 8]])
    [[13, 16, 19]]

    >>> matrix_mul([1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5,6]])
    [[22, 28], [49, 64]]

    >>> matrix_mul([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[30, 36, 42], [66, 81, 96]]

    #Error test cases
    >>> matrix_mul([1, 2], [[3, 4], [5, 6]])
    Traceback (most recent call last):
    TypeError: m_a must be a list or m_b must be a list

    >>> matrix_mul([[1, 2], [3, 4]], [3, 4])
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists or m_b must be a list of lists

    >>> matrix_mul([], [])
    Traceback (most recent call last):
    ValueError: m_a can't be empty or m_b can't be empty

    >>> matrix_mul([[1, 2], [3, "four"]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: m_a should contain only integers or floats

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3]])
    Traceback (most recent call last):
    TypeError: each row of m_b must be of the same size

    >>> matrix_mul([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]])
    Traceback (most recent call last):
    ValueError: m_a and m_b can't be multiplied

    """

if __name__ == "__main__":
    doctest.testmod()
