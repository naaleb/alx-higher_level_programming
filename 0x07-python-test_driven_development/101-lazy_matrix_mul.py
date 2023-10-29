#!/usr/bin/python3
"""
A function that multiply two matrics usning numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices"""
    return numpy.matmul(m_a, m_b)
