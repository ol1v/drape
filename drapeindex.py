"""
DRAPE Index v1.0, MIT License
A simple heuristic metric to score detection performance using TP/FP counts.
Authors: Alex Teixeira, 2025 (initial release)

For more info: https://github.com/inodee/drape

"""

import math

def drape_index(tp, fp, k=0.20, w=0.38, empty_value=None):

    """
    Parameters
    ----------
    tp, fp : int 
        True positives and false positives counts
    k : float
        FP penalty weight
    w : float
        Precision reward weight
    empty_value : any
        What to return when tp + fp == 0

    Returns
    -------
    (score * 10) rounded to 2 decimals, or empty_value

    """
 
    # Empty value treatment
    if tp + fp == 0:
        return empty_value

    # Precision term
    precision = tp / (tp + fp)

    # Avoid exceptions from log10
    tlog = math.log10(tp + 1.0)
    flog = math.log10(fp + 1.0)

    # Calculate score
    score = (tlog * (1.0 + w * precision)) - ((k * flog) / (tlog + 1.0))

    # Round after multiplying by 10
    return round(score * 10.0, 2)

# A few tests
print(drape_index(0, 10, empty_value="-"))
print(drape_index(1, 10, empty_value="-"))
print(drape_index(5, 10, empty_value="-"))
print(drape_index(10, 1, empty_value="-"))
print(drape_index(50, 10, empty_value="-"))
print(drape_index(100, 100, empty_value="-"))
print(drape_index(1000, 100, empty_value="-"))
print(drape_index(0, 150, empty_value="-"))
print(drape_index(100, 0, empty_value="-"))

# The "Zero Line"
print(drape_index(1, 90, empty_value="-"))
print(drape_index(1, 100, empty_value="-"))
print(drape_index(1, 105, empty_value="-"))

