"""
Koan to learn annotating the Python dictionary
"""
from collections import defaultdict
from typing import DefaultDict

# Annotate the dictionary
# Documentation: https://docs.python.org/3/library/typing.html#typing.Dict
result: DefaultDict[str, int] = defaultdict(int)
words: list[str] = [
    "welcome",
    "to",
    "the",
    "world",
    "world",
    "is",
    "an",
    "uneven",
    "place",
]
for word in words:
    result[word] += 1

print(result)
