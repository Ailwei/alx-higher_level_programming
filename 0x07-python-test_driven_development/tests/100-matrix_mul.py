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
    
    # Add more test cases here...

    """

if __name__ == "__main__":
    doctest.testmod()
