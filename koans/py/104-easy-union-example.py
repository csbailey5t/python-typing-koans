"""
Koan to learn annotating data as Union type
"""
# Union says the value can be one of the annotated types.
# Documentation: https://docs.python.org/3/library/typing.html#typing.Union
from typing import Union


vals: list[Union[int, float, str]] = [1, 2.6, "23"]

# Annotate the twice variable to be union of types
twice: list[Union[int, float, str]] = [val * 2 for val in vals]
