import os

import numpy as np


def read_square_matrix(matrix_file) -> np.ndarray:
    matrix = []
    row_counter = 0
    while row_counter < matrices_size:
        line = matrix_file.readline()
        assert isinstance(line, str)
        if not line.isspace():
            row_counter += 1
            matrix_row = [int(element) for element in line.split(sep=' ') if element != '']
            matrix.append(matrix_row)
    return np.array(matrix)


with open(os.path.join('../', 'res', 'data', 'had4.dat'), mode='r') as file:
    matrices_size = int(file.readline())
    distance_matrix = read_square_matrix(file)
    flow_matrix = read_square_matrix(file)
