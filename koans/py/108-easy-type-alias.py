"""
Koan to learn using type-aliases to improve readability
"""

# Annotate the two variables `Line` and `Words` as type aliases. Type Aliases increase the code understanding better.
# Documentation: https://docs.python.org/3/library/typing.html#type-aliases
Line = str
Word = str
Words = list[Word]


def get_words(line: Line) -> Words:
    words = []
    for word in line.split():
        word = word.replace(",", "").replace(".", "").lower()
        words.append(word)
    return words


line: Line = (
    "It was the best of times"
    "it was the worst of times,"
    "it was the age of wisdom,"
    "it was the age of foolishness"
)
print(get_words(line))
