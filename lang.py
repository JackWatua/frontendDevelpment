from random import randint
language = [
    "python",
    "php",
    "javascript",
    "dart",
    "sql",
]


def choose_language():
    return language[randint(0, len(language) - 1)]


print(choose_language())