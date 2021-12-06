import numpy as np


def calculate(input):
    if len(input) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.reshape(np.array(input), (3, 3))
    res = dict()

    res |= {
        'mean': [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix.flatten()).tolist()
        ]
    }
    res |= {
        'variance': [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix.flatten()).tolist()
        ]
    }
    res |= {
        'standard deviation': [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix.flatten()).tolist()
        ]
    }
    res |= {
        'max': [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix.flatten()).tolist()
        ]
    }
    res |= {
        'min': [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix.flatten()).tolist()
        ]
    }
    res |= {
        'sum': [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix.flatten()).tolist()
        ]
    }

    return res
