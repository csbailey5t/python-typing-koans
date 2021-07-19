"""
Koan to learn annotating the Python list of various type of elements
"""
# Annotate mixed type-values. There are two-ways to annotate this
from typing import Union


nos: list[Union[int, float]] = [1, 2.0, 3.5]

# Annotate the list of int to list of better types
squares: list[Union[int, float]] = [no * no for no in nos]
