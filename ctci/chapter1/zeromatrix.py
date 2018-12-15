"""Solution to 1.8: Zero Matrix."""

import numpy as np 


def write_zeros(matrix):
    """Replaces all rows and columns with zeros who contain an element with 0.
    
    Args:
        matrix: an MxN numpy array

    Returns:
        an MxN numpy array with properly zeroed out columns and rows
    """  
    for index, value in np.ndenumerate(matrix):
        if value == 0:
            matrix[index[0], 0] = -1
            matrix[0, index[1]] = -1
    
    for index, value in np.ndenumerate(matrix[0]):
        if value == -1:
            matrix[:, index] = 0

    for index, value in np.ndenumerate(matrix[:, 0]):
        if value == -1:
            matrix[index] = 0
    return matrix