# gameparser.py

import string

stop_words = ["the", "in", "on", "at", "to", "my"]

def remove_punct(text):
    """Remove punctuation from a string."""
    return ''.join(c for c in text if c not in string.punctuation)

def remove_spaces(text):
    """Remove leading and trailing spaces."""
    return text.strip()

def normalise_input(user_input):
    """
    Normalise input: remove punctuation, lowercase, remove stop words, split.

    >>> normalise_input("Take the lamp, please!")
    ['take', 'lamp', 'please']
    >>> normalise_input("Go SOUTH!!")
    ['go', 'south']
    """
    cleaned = remove_punct(user_input).lower().split()
    return [w for w in cleaned if w not in stop_words]
