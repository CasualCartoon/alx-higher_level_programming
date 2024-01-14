import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Resulting matrix.

    Raises:
        ValueError: If matrices cannot be multiplied.
        TypeError: If matrices are not lists of lists or if elements are not integers or floats.
    """
    if not all(isinstance(m, list) for m in (m_a, m_b)):
        raise TypeError("m_a and m_b must be lists of lists")

    try:
        result = np.dot(np.array(m_a), np.array(m_b)).tolist()
        return result
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except TypeError as e:
        raise TypeError("m_a and m_b should contain only integers or floats") from e
