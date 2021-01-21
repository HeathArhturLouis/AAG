from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Word:
    """
    Word of symbols in a set.each with a
    corresponding index/power of 1(False) or -1(True)
    """

    elements: list
    indices: list[bool]

    def reduction(self):
        """Remove reducible pairs from word"""
        # Search for reducible pair
        for i in range(len(self.elements) - 1):
            if (self.elements[i] == self.elements[i + 1]) and (
                self.indices[i] != self.indices[i + 1]
            ):
                # If reducible pair found, remove and call recursively
                self.elements = self.elements[:i] + self.elements[i + 2 :]
                self.indices = self.indices[:i] + self.indices[i + 2 :]
                self.reduction()
                break

    def __mul__(self, other: Word) -> Word:
        """ Returns concatenation (*) of two words without changing either."""
        return Word(self.elements + other.elements, self.indices + other.indices)

    def __invert__(self):
        """Return word with all elements inverted"""
        return Word(
            [e for e in reversed(self.elements)],
            [i for i in reversed([not ind for ind in self.indices])],
        )

    def __eq__(self, other):
        """Check equivalence of words (NOT value)"""
        # TODO: Reduction?
        return (self.elements == other.elements) and (self.indices == other.indices)

    def __len__(self):
        assert len(self.elements) == len(self.indices)
        return len(self.elements)

    def __str__(self):
        p_str = ""
        for i in range(len(self)):
            p_str += " " + str(self.elements[i])
            if self.indices[i]:
                p_str += "^{-1}"
            p_str += " "
        return p_str
